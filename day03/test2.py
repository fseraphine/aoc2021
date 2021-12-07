import time
import tracemalloc

starttime = time.time()
tracemalloc.start()

iterate_ox = lambda _data, ind: sum([int(item[ind]) for item in _data]) * 2 >= len(_data)
iterate_co = lambda _data, ind: sum([int(item[ind]) for item in _data]) * 2 < len(_data)

def iterate(lamb):
    data = [i.rstrip() for i in open('ex_day03.txt', 'r').readlines()]

    for x in range(len(data[0])):
        data_p = lamb(data, x)
        data = [i for i in data if int(i[x]) == data_p]

        if len(data) == 1:
            return data[0]

ox = int(iterate(iterate_ox), 2)
co = int(iterate(iterate_co), 2)
print(ox * co)

endtime = time.time()

print("===========================")
print(f"Temps d'éxécution: {endtime-starttime:0.6f}")
print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())