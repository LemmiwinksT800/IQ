import random
import time
g = ["-", "+"]
start = time.time()
problem = 0
S = 0
for i in range(5):
    now = time.time()
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    c = random.choice(g)
    if c == "-":
        print(f"{a} - {b} = ")
        d = a - b
    if c == "+":
        print(f"{a} + {b} = ")
        d = a + b
    h = 0
    while h != d:
        h = int(input())
        if h == d:
            break
        print("Wrong answer, попробуй ещё раз!")
        problem += 1
    f = round(time.time() - now, 3)
    S += f
    print(f"Accepted, TIME: {f}s")
ex = round(time.time() - start, 3)
print("""_______________________________________""")
print(f"Всего затрачено времени - {ex}s\nСреднее время выполнения - {S / 5}s\nВсего ошибок - {problem}")