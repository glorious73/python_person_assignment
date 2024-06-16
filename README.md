# Introduction
This is the solution for assignment 6 in the python programming course.

# Problem Statement
Write a code that defines the class `Person` which has three object properties and 2 methods as the recorded video. Then add a property called `experience` and a method called `years()`, so that the output for the persons, `Jessa` and `Jon`, will be as below:
```
She works as a Engineer in ABC Company
She studies 10 hours a week
She has more experience years
He works as a Doctor in XYZ Hospital
He studies 15 hours a week
He has less experience years
```

# Solution
A class with the name `Person` was created which looks like this:
```py
class Person:
    def __init__(self, name, sex, profession, experience):
        self.name = name
        self.sex = sex
        self.profession = profession
        self.experience = experience
    
    def work(self, company):
        return f"{"She" if "f" in self.sex.lower() else "He"} works as a {self.profession} in {company}"

    def study(self, hours):
        return f"{"She" if "f" in self.sex.lower() else "He"} studies {hours} hours a week"

    def years(self, pivot):
        return f"{"She" if "f" in self.sex.lower() else "He"} has {"less" if self.experience < pivot else "more"} experience years"
```

and `main` script was created in the same directory which imports the Person file and runs its functions:
```py
from person import Person

def __main__():
    jessa = Person("Jessa", "Female", "Engineer", 5)
    jon = Person("Jon", "Male", "Doctor", 3)
    pivot = 4

    print(jessa.work("ABC Company"))
    print(jessa.study(10))
    print(jessa.years(pivot))

    print(jon.work("XYZ Hospital"))
    print(jon.study(15))
    print(jon.years(pivot))


__main__()
```

# How to run
1. Navigate to the root directory of the project.
2. Open a terminal.
3. Run `python main.py` or `python3 main.py` depending on your installation.
4. The output will be as shown above in the problem statement.