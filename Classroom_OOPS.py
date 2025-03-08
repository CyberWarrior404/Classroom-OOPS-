class Classroom():
    def __init__(self,not_verysmart,average,Smart,teacher,principle):
        self.ns=not_verysmart
        self.avrg=average
        self.Smrt=Smart
        self.t=teacher
        self.p=principle
        print(not_verysmart)
    def definton_of_class(self):
        print("not_verysmart")
        print("average")
        print("Smart")
        print("teacher")
        print(self.ns)
object=Classroom("D","B","A/A+","he/she does the grades","Mr.Bobbyilius")

print(object.definton_of_class())
print(object.not_verysmart)
print(object.average)
print(object.Smart)
print(object.teacher) 