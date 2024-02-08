payRate = float(input("Ingrese el pago por hora $: "))
hourRate = float(input("Ingrese las horas trabajadas: "))

overtimeHours = 0

if (hourRate > 40):
    overtimeHours = hourRate - 40
    totalPay = (40 * payRate) + (overtimeHours * (payRate * 2))

else:
    totalPay = hourRate * payRate

print("")
print("**********************************")
print(f"El seuldo a pagar es {totalPay}")
print("**********************************")

print("For #1")
for n in range(4):
    print (n)

print("**********************************")

print("For #2")
for n in range(1, 4):
    print (n)

print("**********************************")

print("While #3")
n = 0
while (n < 4):
    print (n)
    n += 1
    