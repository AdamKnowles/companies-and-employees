class Pizza:

    def __init__(self):
        self.size = ""
        self.crust_type = ""
        self.toppings = []
       
    def add_topping(self, topping):
        self.toppings.append(topping)

    def print_string(self):
        string = " and ".join(self.toppings)
        print(f'Give me a {self.size} inch pizza that is {self.crust_type} crust with {string}')

pepperoni = Pizza()
pepperoni.size = "16"
pepperoni.crust_type = "thin"
pepperoni.add_topping("pepperoni")
pepperoni.add_topping("olives")
pepperoni.print_string()




    