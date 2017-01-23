""" 
Dette er en kort eksempelkode for å illustrere arv som ble brukt på
gruppetimen den 23.01 2017
"""
class Kurv:
	def tell_items(self):
		pass

class Frukt:
	def __init__(self):
		self.weight = 5
		self.condition = "Good"
	def tell(self):
		print(self.weight)
		print(self.condition)

class Eple(Frukt):
	def __init__(self):
		Frukt.__init__(self)
		self.farge = "Gul"
	def tell(self):
		print("Foo")

class Appelsin(Frukt):
	def __init__(self):
		Frukt.__init__(self)
		self.Vitaminer = ["C","D"]
	


frukt = Frukt()
eple = Eple()
appelsin = Appelsin()

frukt.tell()
eple.tell()
appelsin.tell()	
	

