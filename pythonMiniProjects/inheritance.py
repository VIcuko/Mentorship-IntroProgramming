class Parent():
	def __init__(self, last_name, eye_color):
		self.last_name = last_name
		self.eye_color = eye_color

class Child(Parent):
	def __init__(self, last_name, eye_color, number_of_toys):
		Parent.__init__(self, last_name, eye_color)
		self.number_of_toys = number_of_toys


father = Parent("Maverick","blue")
print (father.last_name, father.eye_color)

little_kid = Child("Maverick","green",10)
print (little_kid.last_name, little_kid.eye_color, little_kid.number_of_toys)