t80 = [0.404, 0.404, 0.405, 0.395, 0.404, 0.401]
t40 = [0.283, 0.283, 0.274, 0.238, 0.292, 0.282]
t20 = [0.200, 0.199, 0.195, 0.199, 0.196, 0.199]

import math

a80 = round(sum(t80) / len(t80), 3)
a40 = round(sum(t40) / len(t40), 3)
a20 = round(sum(t20) / len(t20), 3)

s80 = round(sum([(x - a80) ** 2 for x in t80]) / len(t80), 6)
s40 = round(sum([(x - a40) ** 2 for x in t40]) / len(t40), 6)
s20 = round(sum([(x - a20) ** 2 for x in t20]) / len(t20), 6)

for i in range(0, len(t80)):
    print(f"    & {t80[i]} & {t40[i]} & {t20[i]} \\\\")

print(f"    & ===== & ===== & ===== \\\\")
print(f"    Mittelwert & {a80} & {a40} & {a20} \\\\")
print(f"    Standardabweichung & {s80:.6f} & {s40:.6f} & {s20:.6f}")

print("".join([f"({x},{y})" for x, y in enumerate(t80)]))
print("".join([f"({x},{y})" for x, y in enumerate(t40)]))
print("".join([f"({x},{y})" for x, y in enumerate(t20)]))
