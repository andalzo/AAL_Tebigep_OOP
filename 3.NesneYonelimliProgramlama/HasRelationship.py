class Employer:

    def __init__(self, name: str, salary: float):
        self.name: str = name
        self.salary: float = salary


class Company:

    def __init__(self, name: str, monthly_income: float):
        self.name: str = name
        self.employer_list: list[Employer] = list()
        self.monthly_income: float = monthly_income

    def add_employer(self, employer: Employer):
        self.employer_list.append(employer)

    def show_net_income(self) -> float:
        total_expenses = 0
        for employer in self.employer_list:
            total_expenses += employer.salary
        return total_expenses - self.monthly_income


def main():
    employer1 = Employer("Enes Sancak", 15000)
    employer2 = Employer("John Doe", 6000)

    company_A = Company("A", 20000)
    company_A.add_employer(employer1)
    company_A.add_employer(employer2)

    print(f"The net income of company A is {company_A.show_net_income()}")


if __name__ == "__main__":
    main()
