# assignment 3 part 1
from telnetlib import DO


class Dog:
    def __init__(self, name, breed = 'mutt', weight = 0):
        # what do we need to put in the init?
        # the init should take in name, breed (defaults to 'mutt' if none provided,
        # and weight (defaults to 0 if none provided))
        self.name = name
        self.breed = breed
        self.weight = weight

    def lastName(self):
        # should return the last name of the dog (split the name into first and last, return last)
        return self.name.split(' ')[1]
    
    def __str__(self):
        # should return this list for example: [Dog: Bob Smith, breed: mutt, weight: 0]
        return "[Dog: {}, breed: {}, weight: {}]".format(self.name, self.breed, self.weight)


class Kennel:
    def __init__(self, *args):
        self.members = list(args)
        
    def addMember(self, dog):
        # this method should append a dog to the list of members
        self.members.append(dog)
        
    def delMember(self,dog):
        # this method should remove a dog from the list of members
        self.members.remove(dog)
        
    def showAll(self):
        # this method should print "\nDogHouse Kennel visiting dogs:" and 
        # then a list of all the dogs in the kennel (all members)
        print("\nDogHouse Kennel visiting dogs:")
        for doggo in self.members:
            print(doggo)

            
if __name__ == '__main__':
    # I prefer to use the "".format method
    bob = Dog('Bob Smith')
    sue = Dog('Sue Jones', breed='Weimaraner', weight=30)
    print("Bob:  {}".format(bob))
    print("Bob lastname:  {}, Sue lastname:  {}".format(bob.lastName(), sue.lastName()))
    print("Sue:  {}".format(sue))
    fido = Dog('Fido McAurthur',breed='German Shorthair',weight=60)
    
    DogHouse = Kennel(bob, sue)          
    DogHouse.addMember(fido)
    DogHouse.showAll()                      
    DogHouse.delMember(bob)
    DogHouse.showAll()


'''
When this code runs, it should produce this output exactly:
    
Bob:  [Dog: Bob Smith, breed: mutt, weight: 0]
Bob lastname:  Smith , Sue lastname:  Jones
Sue:  [Dog: Sue Jones, breed: Weimaraner, weight: 30]

DogHouse Kennel visiting dogs:
[Dog: Bob Smith, breed: mutt, weight: 0]
[Dog: Sue Jones, breed: Weimaraner, weight: 30]
[Dog: Fido McAurthur, breed: German Shorthair, weight: 60]

DogHouse Kennel visiting dogs:
[Dog: Sue Jones, breed: Weimaraner, weight: 30]
[Dog: Fido McAurthur, breed: German Shorthair, weight: 60]

'''