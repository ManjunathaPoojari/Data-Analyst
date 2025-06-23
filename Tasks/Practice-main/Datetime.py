m, d, y = input().split()
m = int(m)
d = int(d)
y = int(y)
if m < 3:
    m = m + 12
    y = y - 1
K = y % 100
J = y // 100
f = d + 13*(m + 1)//5 + K + K//4 + J//4 + 5*J
day_index = f % 7
days = ["SATURDAY", "SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
print(days[day_index])
