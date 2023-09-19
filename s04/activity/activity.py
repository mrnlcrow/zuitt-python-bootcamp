class Camper():
	#attributes (properties)
	def __init__(self,name,batch,course_type):
		self.name=name
		self.batch=batch
		self.course_type=course_type

	#methods
	def career_track(self):
		print(f"Currently enrolled in the {self.course_type} program.")

	def info(self):
		print(f"My name is {self.name} of batch {self.batch}.")

zuitt_camper=Camper('Mrinal',2023,'BEC004')
print("Camper name: "+zuitt_camper.name+"\n"+"Camper Batch: "+str(zuitt_camper.batch)+"\n"+"Camper Course: "+zuitt_camper.course_type)
zuitt_camper.info()
zuitt_camper.career_track()


