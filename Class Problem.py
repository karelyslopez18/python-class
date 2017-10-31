class Pet(object):
    def __init__(self, name, animal_type, age):
        self.name = name
        self.animal_type = animal_type
        self.age = age

    def set_name(self, name):
        self.name = name

    def set_type(self, animal_type):
        self.animal_type = animal_type

    def set_age(self, age):
        self.age = age

    def get_name(self):
        return self.name

    def get_animal_type(self):
        return self.animal_type

    def get_age(self):
        return self.age
    
    def info(self):
        return 'The pet name is', self.name, 'The type is', self.animal_type, 'The age is', self.age

def main():

    name = input('What is the name of the pet: ')
    animal_type = input('What type of pet is it: ')
    age = int(input('How old is your pet: '))

    
    pets = Pet(name, animal_type, age)
    print('The information will be added to the records.')
    print('The data you entered is')
    print(pets.info())
main()

