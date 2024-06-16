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