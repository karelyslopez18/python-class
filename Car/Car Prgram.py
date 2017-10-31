import Car

def program():

    print ("Car is Accelerating ")
    for i in range(5):
        my_car.accelerate()
        print ("Current speed ", my_car.getSpeed())
  
    print ("Car is braking ")
    for i in range(5):
        my_car.brake()
        print ("Current speed ", my_car.getSpeed())

    print("Car values are:\n", my_car)
