
class Student:

    def __init__(self, name: str, no: int, note: float):
        self.name = name
        self.no = no
        self.note = note

    def change_note(self, new_note: float):
        self.note = new_note


student1 = Student("Enes Sancak", 1401, 88.5)
student2 = Student("John Doe", 1402, 66)

student1.change_note(90.0)
student2.change_note(76)

print(f"{student1.name} Note: {student1.note}")
print(f"{student2.name} Note: {student2.note}")
