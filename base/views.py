from django.shortcuts import render
from .forms import InsuranceForm
from .expertaSys import InsuranceQuote, InsurancePricingEngine

# Create your views here.


def home(request):
    if request.method == "POST":
        form = InsuranceForm(request.POST)
        if form.is_valid():
            return result(request)
    else:
        form = InsuranceForm()

    return render(request, 'base/home.html', {"form": form})


def result(request):
    form = InsuranceForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data

        engine = InsurancePricingEngine()

        engine.reset()
        engine.declare(InsuranceQuote(
            age=data['age'],
            gender=data['gender'],
            vehicle_type=data['vehicle_type'],
            insurance_type=data['insurance_type'],
            vehicle_price=float(data['vehicle_price']),
            mileage_per_year=data['mileage_per_year'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            previous_insurance=data['previous_insurance'],
            previous_accidents=data['previous_accidents'],
            country=data['country'],
            city=data['city'],
        ))

        engine.run()
        premium = engine.get_price()

        return render(request, 'base/result.html', {"result": premium})

    return render(request, 'base/home.html', {"form": form})
