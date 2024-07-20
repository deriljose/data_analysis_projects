import mean_var_std

list1 = []

for i in range(9):
    list1.append(int(input("Enter a number: ")))

print(mean_var_std.calculate(list1))