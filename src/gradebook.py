class Gradebook:
    def __init__(self):
        self.students = {}

    def add_student(self, name: str):
        if name in self.students:
            raise ValueError("Student already exists")
        self.students[name] = []

    def add_grade(self, name: str, grade: int):
        if name not in self.students:
            raise KeyError("Student not found")
        if not (1 <= grade <= 5):
            raise ValueError("Grade must be between 1 and 5")
        self.students[name].append(grade)

    def get_student_average(self, name: str) -> float:
        if name not in self.students:
            raise KeyError("Student not found")
        grades = self.students[name]
        if not grades:
            return 0.0
        return sum(grades) / len(grades)

    def get_excellent_students(self) -> list:
        excellent = []
        for name, grades in self.students.items():
            if grades and (sum(grades) / len(grades)) >= 4.5:
                excellent.append(name)
        return excellent

    def remove_student(self, name: str):
        if name in self.students:
            del self.students[name]
