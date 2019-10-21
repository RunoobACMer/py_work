class Dog():
	
	def __init__(self,name,age):
		self.name = name
		self.age = age
		
	def sit(self):
		print(self.name.title() + " is sitting !")
	
	def rool_over(self):
		print(self.name.title() + " is roving !")
		
dog = Dog('white', 6)
dog.sit()
dog.rool_over()
