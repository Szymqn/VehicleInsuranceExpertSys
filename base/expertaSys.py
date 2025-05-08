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
        self.info_list = []
        self.info_list.append(f"Starting price : {self.price}\n")

    @Rule(InsuranceQuote(vehicle_price=MATCH.price, insurance_type='OC'))
    def base_oc(self, price):
        self.price += 0.03 * price
        self.info_list.append(f"Chosen Insurance Type: OC. Price is increased by 3%. Current price: {self.price}\n")

    @Rule(InsuranceQuote(vehicle_price=MATCH.price, insurance_type='OC + NNW'))
    def base_oc_nnw(self, price):
        self.price += 0.045 * price
        self.info_list.append(f"Chosen Insurance Type: OC + NNW. Price is increased by 4.5%. Current price: {self.price}\n")
    @Rule(InsuranceQuote(vehicle_price=MATCH.price, insurance_type='OC + AC + NNW'))
    def base_full(self, price):
        self.price += 0.06 * price
        self.info_list.append(f"Chosen Insurance Type: OC + AC + NNW. Price is increased by 6%. Current price: {self.price}\n")
    @Rule(InsuranceQuote(age=P(lambda x: x < 25)))
    def young_driver_surcharge(self):
        self.price *= 1.25
        self.info_list.append(f"The insurance is being calculated for a young driver. Price is increased by 25%. Current price: {self.price}\n")
    @Rule(InsuranceQuote(age=P(lambda x: x > 50)))
    def experienced_driver_discount(self):
        self.price *= 0.9
        self.info_list.append(f"The insurance is being calculated for an experienced driver . Price is increased by 3%. Current price: {self.price}\n")
    @Rule(InsuranceQuote(previous_accidents=P(lambda x: x > 0)))
    def accident_surcharge(self):
        self.price += 200
        self.info_list.append(f"Previous accidents were detected. Price is increased by 200. Current price: {self.price}\n")
    @Rule(InsuranceQuote(previous_accidents=P(lambda x: x >= 3)))
    def many_accidents_penalty(self):
        self.price *= 1.5
        self.info_list.append(f"More than 3 accidents were detected. Price is increased by 50%. Current price: {self.price}\n")
    @Rule(InsuranceQuote(vehicle_type='motorcycle'))
    def motorcycle_risk(self):
        self.price *= 1.2
        self.info_list.append(f"Chosen vehicle type is a motorcycle. Price is increased by 20%. Current price: {self.price}\n")
    @Rule(InsuranceQuote(previous_insurance=True, previous_accidents=0))
    def safe_driver_discount(self):
        self.price *= 0.85
        self.info_list.append(f"No previous accidents. Price is decreased by 15%. Current price: {self.price}\n")
    @Rule(InsuranceQuote(mileage_per_year=P(lambda x: x > 25000)))
    def high_mileage_penalty(self):
        self.price += 100
        self.info_list.append(f"High yearly mileage. Price is increased by 100. Current price: {self.price}\n")
    @Rule(InsuranceQuote(mileage_per_year=P(lambda x: x < 8000)))
    def low_mileage_discount(self):
        self.price *= 0.95
        self.info_list.append(f"Low yearly mileage. Price is decreased by 5%. Current price: {self.price}\n")
    def get_price(self):
        return round(self.price, 2), self.info_list
