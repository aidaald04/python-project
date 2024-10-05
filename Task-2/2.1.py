N = int(input("Введите количество школьников: "))
K = int(input("Введите количество мандаринов: "))

tangerines_per_student = K // N
remainingtangerines = K % N

print(tangerines_per_student)
print(remainingtangerines)
