class person:
    def __init__(self, name, age,education):
        self.name = name
        self.age  = age
        self.education = education
class Child_class(person):
    pass


person_reza = Child_class("reza", 15, "diplom")
person_ali = person("ali", 24, "Bachelor's degree")


print(person_reza.education)
print(person_reza.name)
print(person_reza.age)

print("------------------")




print(person_ali.name)
print(person_ali.age)