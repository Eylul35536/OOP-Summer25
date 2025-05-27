class Car:
    def __init__(self, brand, engine_type):
        self.brand = brand
        
        self.__engine_type = engine_type

    def show_engine_type(self):
        print(f"Engine type: {self.__engine_type}")

    
    def __start_the_engine(self):
        print("Engine started... Vınn!")


    def start_the_car(self):
        print(f"Starting {self.brand}")
        self.__start_the_engine()

my_car = Car('Audi', 'RS7')

print(my_car.brand)                 
my_car.show_engine_type()         
my_car.start_the_car()            