
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")


position = input("Where do you want to put the treasure? ")
position = list(position)

linha =int(position[0])
coluna =int(position[1])

linha = linha -1
coluna =coluna -1
map[coluna][linha] = " X"
print(f"{row1}\n{row2}\n{row3}")









