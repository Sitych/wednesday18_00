class SchoolClass:

     def __init__(self, students, name):
          self.stds = students
          self.name = name

     def math_mark(self, marks):
          self.mark = marks

     def sort_by_marks(self):
          for i in range(len(self.stds)):
               for f in range(len(self.stds) - 1):
                    if self.mark[f] > self.mark[f + 1]:
                         self.stds[f], self.stds[f + 1] = self.stds[f + 1] , self.stds[f]
                         self.mark[f], self.mark[f + 1] = self.mark[f + 1] , self.mark[f]
                         

students = ["Кирилл", "Валера", "Egor", "Sasha"]

python = SchoolClass(students, "11Е")
python.math_mark([7, 5, 9, 6])
python.sort_by_marks()
print(python.stds)
