#some thoughts about what i learned
calculo = []
wanted = input("what do you want to calculate? ")

d = wanted.split()

print(d)

for i in d:
    if i in ['+', '-', '/', '*']:
        calculo.append(i)
    else:
        calculo.append(int(i))


print (calculo)

expression = ' '.join(map(str, calculo))

print(expression)

result = eval(expression)

print(f"the result of the expression {expression} is: {result}")





