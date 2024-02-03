from StudentClass_Enhanced import Student


def main():
    student = Student()
    student.set_name("Enes Sancak")
    student.__name = "Enes Sancak" # Gives an error here, because this is a private field
    student.set_no(1401)
    student.set_notes([87.6, 90, 67, 80.57])

    print(f"Student No: {student.get_no()}, Note Average: {student.get_average()}")


if __name__ == "__main__":
    main()
