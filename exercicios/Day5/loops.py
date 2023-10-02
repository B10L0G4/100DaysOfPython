student_heights = input("Input a list of student heights ").split()

print(student_heights)
total = 0

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total = total + student_heights[n]

print(total)

media = round(total / (n +1))
print(media)


#180 124 165 173 189 169 146