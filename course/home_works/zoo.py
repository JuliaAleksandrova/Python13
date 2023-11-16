class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

class Mammal(Animal):
	def __init__(self, name, species, fur_color):
		super().__init__(name, species)
		self.fur_color = fur_color

class Bird(Animal):
	def __init__(self, name, species, wing_span):
		super().__init__(name, species)
		self.wing_span = wing_span

class Reptile(Animal):
	def __init__(self, name, species, scale_type):
		super().__init__(name, species)
		self.scale_type = scale_type


class Zoo:
	def __init__(self):
		self.animals = []

	def add_animal(self, animal):
		self.animals.append(animal)

	def list_animals(self):
		return [animal.name for animal in self.animals]

	def get_animals_by_species(self, species):
		animals_by_species = []
		for animal in self.animals:
			if animal.species == species:
				animals_by_species.append(animal.name)
		return animals_by_species

	def remove_animal(self, name):
		for animal in self.animals:
			if animal.name == name:
				self.animals.remove(animal)

	def count_animals(self,):
		return len(self.animals)


# # You can use code below for testing purpouses if you want
# if __name__ == "__main__":
zoo = Zoo()

lion = Mammal('Simba', 'Lion', 'Golden')
eagle = Bird('Baldy', 'Eagle', 100)
python = Reptile('Monty', 'Python', 'Diamond')
royal_python = Reptile('Muscle', 'Python', 'Triangle')

zoo.add_animal(lion)
zoo.add_animal(eagle)
zoo.add_animal(python)
zoo.add_animal(royal_python)

print('Zoo animals:')
print(zoo.list_animals())

#     print('Feeding animals:')
#     zoo.feed_animals()
#
print('Removing animal:')
zoo.remove_animal("Baldy")
print(zoo.list_animals())
#print('Zoo animals after removing:')
#zoo.list_animals()
#
print('Total number of animals', zoo.count_animals())
#
#     print('List all reptiles:')
#     reptiles = zoo.get_animals_by_species('Python')
#     for reptile in reptiles:
#         print(f'{reptile.get_name()} ({reptile.get_species()})')