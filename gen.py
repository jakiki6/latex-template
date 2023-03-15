t1 = [0.363, 0.255, 0.237, 0.177, 0.115, 0.144, 0.094, 0.189, 0.036, 0.181]
t2 = [3.594, 2.551, 2.368, 1.766, 1.153, 1.440, 1.872, 1.876, 1.689, 1.804]

import math

v1 = [round(0.1 / x, 3) for x in t1]
v2 = [round(1.0 / x, 3) for x in t2]

d = [abs(x - y) / (0.5 * (x + y)) for x, y in zip(v1, v2)]

for i in range(0, len(t1)):
    print(f"    {t1[i]} & {t2[i]} & {v1[i]} & {v2[i]} & {round(d[i] * 100, 3)}\\% \\\\")
