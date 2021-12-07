data = [i.rstrip() for i in open('ex_day03.txt', 'r').readlines()]

data_p = [int(sum([int(item[i]) for item in data]) * 2 > len(data)) for i in range(len(data[0]))]

_max = int('1'*len(data[0]),2)

num = ''
for bit in data_p:
    num += str(bit)
print(num)

num = int(num, 2)
print(num)
num2 = _max - num
print(num2)
print(num * num2)
