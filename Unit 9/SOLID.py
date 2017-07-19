class Email
	def __init_(self, value):
		self.value = value

	def is_valid(self):
		if '@' in self.value:
			return True

		return False


class Person:
	def __init__(self, email,first_name, last_name):
		self.email = Email(email)
		self.first_name = first_name
		self.last_name = last_name

	p = Person ('tomhanks@gmail.com', 'Tpn', 'Hanks')
	print(p.emial.is_valid())




	# S - single responsibility
	# O - open/closed principle
	# L - liskov substitution
	# I - interface segregation 
	# D - dependency inversion