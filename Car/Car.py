class Car:
    def _init_(self, year_model, make, speed):
        self.year_model = year_model
        self.make = make
        self.speed = speed

    def setYear_model(self, year_model):
        self.year_model = year_model

    def getYear_model(self):
        return self.year_model

    def setMake(self, make):
        self.make = make

    def getMake(self):
        return self.make
    
#Set speed first before getting info of the class
    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def accelerate(self):
        self.speed= speed + 5

    def brake(self):
        self.speed= speed - 5
    
    def info (self):
        return "The Maker is " + self.make + ", The Model Year is " + self.year_model + ", The Speed is " + str(self.speed)
    
def main():

    year=(input('car year: '))
    make=(input('car make: '))
    speed=eval(input('car speed: '))

    my_car= Car(year,make,speed)

    print ("Car is Accelerating...")
    my_car.accelerate(speed)
    print('The current speed is: ', my_car.getSpeed())
    my_car.accelerate(speed)
    print('The current speed is: ', my_car.getSpeed())
    my_car.accelerate(speed)
    print('The current speed is: ', my_car.getSpeed())
    my_car.accelerate(speed)
    print('The current speed is: ', my_car.getSpeed())
    my_car.accelerate(speed)
    print('The current speed is: ', my_car.getSpeed()) 

    
    print ("Car is braking...")
    my_car.brake()
    print('The current speed after brake is: ', my_car.getSpeed())
    my_car.brake()
    print('The current speed after brake is: ', my_car.getSpeed())
    my_car.brake()
    print('The current speed after brake is: ', my_car.getSpeed())
    my_car.brake() 
    print('The current speed after brake is: ', my_car.getSpeed())
    my_car.brake()
    print('The current speed after brake is: ', my_car.getSpeed())

    print('Final speed is:', my_car.getSpeed())

main()
