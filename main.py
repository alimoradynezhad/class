class person:
    def __init__(self, name, age,education):
        self.name = name
        self.age  = age
        self.education = education
class educ(person):
    pass


person_edue = educ("reza", 15, "diplom")
person_ali = person("ali", 24, "Bachelor's degree")


print(person_edue.education)
print(person_edue.name)
print(person_edue.age)

print("------------------")




print(person_ali.name)
print(person_ali.age)