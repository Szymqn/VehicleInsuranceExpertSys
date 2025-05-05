from experta import KnowledgeEngine, Rule, Fact, MATCH, P


class InsuranceQuote(Fact):
    first_name = str
    last_name = str
    email = str
    phone = str
    age = int
    gender = str
    vehicle_type = str
    insurance_type = str
    vehicle_price = float
    mileage_per_year = int
    start_date = str
    end_date = str
    previous_insurance = bool
    previous_accidents = int
    country = str
    city = str


class InsurancePricingEngine(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.price = 2000

    @Rule(InsuranceQuote(vehicle_price=MATCH.price, insurance_type='OC'))
    def base_oc(self, price):
        self.price += 0.03 * price

    @Rule(InsuranceQuote(vehicle_price=MATCH.price, insurance_type='OC + NNW'))
    def base_oc_nnw(self, price):
        self.price += 0.045 * price

    @Rule(InsuranceQuote(vehicle_price=MATCH.price, insurance_type='OC + AC + NNW'))
    def base_full(self, price):
        self.price += 0.06 * price

    @Rule(InsuranceQuote(age=P(lambda x: x < 25)))
    def young_driver_surcharge(self):
        self.price *= 1.25

    @Rule(InsuranceQuote(age=P(lambda x: x > 50)))
    def experienced_driver_discount(self):
        self.price *= 0.9

    @Rule(InsuranceQuote(previous_accidents=P(lambda x: x > 0)))
    def accident_surcharge(self):
        self.price += 200

    @Rule(InsuranceQuote(previous_accidents=P(lambda x: x >= 3)))
    def many_accidents_penalty(self):
        self.price *= 1.5

    @Rule(InsuranceQuote(vehicle_type='motorcycle'))
    def motorcycle_risk(self):
        self.price *= 1.2

    @Rule(InsuranceQuote(previous_insurance=True, previous_accidents=0))
    def safe_driver_discount(self):
        self.price *= 0.85

    @Rule(InsuranceQuote(mileage_per_year=P(lambda x: x > 25000)))
    def high_mileage_penalty(self):
        self.price += 100

    @Rule(InsuranceQuote(mileage_per_year=P(lambda x: x < 8000)))
    def low_mileage_discount(self):
        self.price *= 0.95

    def get_price(self):
        return round(self.price, 2)
