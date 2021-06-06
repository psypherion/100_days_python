# exercise-1
# Student Grading:
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
import time
student_grades = {}
start = time.time()
for i in student_scores :
  if student_scores.get(i) in range (91,100):
    student_grades[i] = "Outstanding"
  if student_scores.get(i) in range (81,90):
    student_grades[i] = "Exceeds Expactation"
  if student_scores.get(i) in range (71,80):
    student_grades[i] = "Acceptable"
  if student_scores.get(i) in range (0,70):
    student_grades[i] = "Fail"
end = time.time()
print("time taken : ",end - start)
print(student_grades)
