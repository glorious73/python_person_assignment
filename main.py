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