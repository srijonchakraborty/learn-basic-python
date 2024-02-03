print("Hi srijon");


age:int = 30;
name: str="Srijon Chakraborty";
height:float=5.6;
is_student=False;

#print("Info of Name:{name}, age:{age}, height:{height}, Studentship Status:{is_student} ")
# letter f is like Console.Writeline($"Name:{name}") like this
print(f"Info of Name: {name}, age: {age}, height: {height}, Studentship Status: {is_student}");

class Person:
    def __init__(self, name: str, age: int, height: float, is_student: bool):
        self.name = name
        self.age = age
        self.height = height
        self.is_student = is_student

    def __str__(self):
        return f"Person(Name: {self.name}, Age: {self.age}, Height: {self.height}, Is Student: {self.is_student})"

# Create an instance of the Person class
person = Person(name, age, height, is_student);
print("Using Class:",person);

class PersonList:
    def __init__(self):
        self.person_list = []

persons= PersonList()

persons.person_list.append(Person("Srijon", 10, 5.6, True));
persons.person_list.append(Person("Roger", 12, 5.8, True));
persons.person_list.append(Person("Jassi", 15, 6, False));

print("------Loop New-------");
for person in persons.person_list:
    print(person);












