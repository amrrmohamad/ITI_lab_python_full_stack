"""
- this sys is responsible for managing cars and motorcycle data
- sell for new and used cars and show
- calculate the sales for the agency , comparing cars [power] and for used cars i can show how much km is move

- renting cars for customers

- buying options
"""


class Race_Car:
    def __init__(self, name, color, model, staus, power, price, day_rent):
        self.name = name
        self.color = color
        self.model = model
        self.staus = staus
        self.day_rent = day_rent
        self.power = int(power)
        self.price = int(price)
        if self.price < 10000:
            print(f"sorry your price '{self.price}$' in not enough")

    def __str__(self):
        return self.name


class Classic_Car:
    def __init__(self, name, color, model, staus, power, price, day_rent):
        self.name = name
        self.color = color
        self.model = model
        self.staus = staus
        self.day_rent = day_rent
        self.power = int(power)
        self.price = int(price)

    def __str__(self):
        return self.name


# ===============================================================================


class Motorcycle:
    def __init__(self, name, color, model, staus, power, price):
        self.name = name
        self.color = color
        self.model = model
        self.staus = staus

        self.power = int(power)
        self.price = int(price)

    def __str__(self):
        return self.name


# ===============================================================================


class Employee:
    def __init__(self, name, salary, commision, role):
        self.name = name
        self.salary = int(salary)
        self.commisison = commision
        self.role = role

    def check(self):
        return self.salary + self.commisison

    def __str__(self):
        return self.name


# ===============================================================================


class Customer(Classic_Car, Race_Car):

    def __init__(self, name, deposit, status):
        self.name = name
        self.deposit = int(deposit)
        self.status = status

    def __str__(self):
        return self.name


# ===============================================================================


class Agancy:

    sales = 0

    def __init__(self):
        self.cars = []
        self.motorcycles = []
        self.selled_cars = []
        self.employees = []

    def insert(self, item):
        if isinstance(item, Race_Car) or isinstance(item, Classic_Car):
            self.cars.append(item)
            print(f"you add this car to your agancy {item}")
        else:
            self.motorcycles.append(item)
            print(f"you add this motorcycle to your agancy {item}")

    def get_all(self, item):
        if item == "cars":
            for car in self.cars:
                print(str(car))
        else:
            for mororcycle in self.motorcycles:
                print(str(mororcycle))

    def sell_this(self, item, customer, employee):
        # add the price for the sales
        self.selled_cars.append(item)
        self.sales += item.price
        self.cars.remove(item)
        # sale=Sell(item,customer)
        commisison = item.price * 0.025
        employee.commisison += commisison
        self.sales -= commisison
        self.employees.append(employee)
        print(
            f"this sell done by {employee.name} for {item} selled to {customer.name} "
        )

    def compare_power(self, car1, car2):
        if isinstance(car1, (Classic_Car, Race_Car)) and isinstance(
            car2, (Classic_Car, Race_Car)
        ):
            if car1.power > car2.power:
                return f"{car1.name} : ({car1.power} PH) is more powerful than {car2.name} : ({car2.power} PH)."
            elif car1.power < car2.power:
                return f"{car2.name} ({car2.power} PH) is more powerful than {car1.name} : ({car1.power} PH)."
            else:
                return f"{car1.name} and {car2.name} have the same power : ({car1.power} PH)."
        else:
            return "Both vehicles must be cars to compare power."

    def rent_car(self, car, customer, rent_days):
        car.is_rented = False
        if car.is_rented:
            return f"Sorry, {car.name} is rented."

        rent_cost = rent_days * car.day_rent

        if customer.deposit < rent_cost:
            return f"not enough deposit for renting {car.name} => Required: ${rent_cost} : Available: ${customer.deposit}"

        car.is_rented = True
        customer.deposit -= rent_cost
        self.sales += rent_cost

        return f"{car.name} rented to {customer.name} for {rent_days} days. Total cost: ${rent_cost}"

    def __str__(self):
        return "i'm agancy for cars and motor cycles"


# ================================================================================

car1 = Classic_Car("toyota", "black", "crola", "new", 200, 5000, 100)
car2 = Race_Car("Ferrari", "red", "F8 spider", "new", 750, 1000, 200)
motorcycle1 = Motorcycle("Harley-Davidson", "Black", "Iron 883", "New", 100, 9000)

agancy = Agancy()
agancy.insert(car1)
agancy.insert(car2)
agancy.insert(motorcycle1)


customer1 = Customer("hamada1", 20000, "cash")
customer2 = Customer("mohamad", 5000, "cash")
empoloyee = Employee("hamada_seller", 500, 0, "seller")

agancy.sell_this(car1, customer1, empoloyee)
agancy.sell_this(car2, customer2, empoloyee)

print("=" * 50)
compare1 = agancy.compare_power(car1, car2)
compare2 = agancy.compare_power(car1, motorcycle1)
compare3 = agancy.compare_power(car2, motorcycle1)
print(compare1, compare2, compare3, sep="\n\n")
print("=" * 50)

rent = agancy.rent_car(car1, customer2, 10)
print(rent, sep="\n")
print("================= sales ==================")
print(agancy.sales)
print(empoloyee.check())
print("==========================================")
print(agancy.get_all("cars"))
