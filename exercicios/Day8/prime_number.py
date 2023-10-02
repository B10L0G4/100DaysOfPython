def prime_number(num):
  if num > 1:
    for i in range(2, num):
      if (num % i) == 0:
        print(num, "não é primo")
        break
    else:
      print(num, "é primo")

  else:
    print(num, "é primo")

number = int(input("Digite um numero "))
prime_number(num = number)











# sum = 0
# for digit in i:
#   sum += int(digit)
# print(sum)







