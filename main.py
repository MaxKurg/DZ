# 1. Практическое задание
q = ["spisok",5.45,7]
print(q)
print(type(q))
for el in q:
    print(type(el))

# 2. Практическое задание
q.append("tur")
print(q)
q[0],q[1] = q[1],q[0]
print(q)
q[2],q[3] = q[3],q[2]
print(q)

# 3. Практическое задание
periud = [1,2,3,4,5,6,7,8,9,10,11,12]
print(periud)
a = periud[0:3]
b = periud[3:6]
c = periud[6:9]
d = periud[9:12]
a = "зима"
b = "весна"
c = "лето"
d = "осень"


r = int(input("введите месяц: "))


if r < 4:
    print(a)
elif r > 3 and r < 7:
    print(b)
elif r > 6 and r <10:
    print(c)
else:
    print(d)
# 4. Практическое задание







