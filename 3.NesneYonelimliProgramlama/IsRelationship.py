class Employer:

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary

    def increase_salary(self):
        self.salary += self.salary * 0.33

    def print_salary(self):
        print(f"Name: {self.name} : Salary: {self.salary}")


class Engineer(Employer):

    def __init__(self, name: str, salary: float):
        super().__init__(name, salary)

    def increase_salary(self):
        self.salary += self.salary * 0.44


class Technician(Employer):

    def __init__(self, name: str, salary: float):
        super().__init__(name, salary)

    def increase_salary(self):
        self.salary += self.salary * 0.25


class Company:

    def __init__(self, name: str):
        self.name: str = name
        self.employer_list: list[Employer] = list()

    def add_employer(self, employer: Employer):
        self.employer_list.append(employer)

    def increase_salaries(self):
        for employer in self.employer_list:
            employer.increase_salary()

    def show_salaries(self):
        for employer in self.employer_list:
            employer.print_salary()


def main():
    employer = Employer("John Doe", 10000)
    engineer = Engineer("Enes Sancak", 10000)
    technician = Technician("Jane Doe", 10000)

    company = Company("Tebigep")

    company.add_employer(employer)
    company.add_employer(engineer)
    company.add_employer(technician)

    company.increase_salaries()
    company.show_salaries()


if __name__ == "__main__":
    main()
