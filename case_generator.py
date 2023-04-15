import random
import os

cases = 20
for i in range(cases):
    N = random.randint(1, 5)
    caseString = "%d\n" % N
    for j in range(N):
        T = random.randint(5, 15)
        arr = ""
        for k in range(T-1):
            arr += f"{random.randint(-100, 100)} "
        caseString += arr + "\n"

    caseName = 'g0.{}.in'.format(i)

    casePath = os.path.join('MiCompaElGymRat/cases', caseName)
    with open(casePath, 'w') as f:
        f.write(caseString.strip('\t\n\r'))
