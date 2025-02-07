class classroom():
    def __init__(self,not_verysmart,average,Smart,teacher):
        self.not_verysmart=not_verysmart
        self.average=average
        self.Smart=Smart
        self.teacher=teacher
    def definton_of_class(self):
        print("not_verysmart")
        print("average")
        print("Smart")
        print("teacher")

object=classroom("D","B","A/A+","he/she does the grades")

print(object.definton_of_class())
print(object.not_verysmart)
print(object.average)
print(object.Smart)
print(object.teacher)