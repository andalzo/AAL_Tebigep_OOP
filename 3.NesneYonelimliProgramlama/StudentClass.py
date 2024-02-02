class Student:

    def __init__(self, name: str, no: int, notes: list[float]):
        self.name = name
        self.no = no
        self.notes = notes

    def calculate_average(self) -> float:
        note_sum = 0.0
        for note in self.notes:
            note_sum += note
        return note_sum / len(self.notes)


def calculate_and_print_average(student: Student):
    print(f"Student Name: {student.name}")
    print(f"Student No: {student.no}")
    print(f"Average Note: {student.calculate_average()}")


def main():
    student1 = Student("Enes Sancak", 1401, [87, 67, 99])
    student2 = Student("John Doe", 131, [56.8, 100, 67])

    calculate_and_print_average(student1)
    calculate_and_print_average(student2)


if __name__ == "__main__":
    main()
