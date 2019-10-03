import pandas as pd
import numpy as np
from scipy.integrate import simps

def Nintegrate(a, b, f):
    x = np.linspace(a, b, 1000)
    y = f(x)
    return simps(y, x)

def f(x):
    return 1 / np.sqrt(0.3 * x + 0.7 * x**4)
x = np.linspace(0.01,1,100)
y1 = 5 * np.log10((1 + x)* (1 - 1 / np.sqrt(1 + x))) + 5 * np.log10(5.99584e8 / 0.72)

y2 = np.zeros_like(y1)
for i in range(len(y1)):
    intv = Nintegrate(1/(1+x[i]), 1, f)
    y2[i] = 5 * np.log10((1+x[i]) * intv)
y2 += 5 * np.log10(2.97792e8/0.72)
data = {'z':x, 'm1':y1, 'm2':y2}
df = pd.DataFrame(data)
df.to_csv('data16_2.csv', index=0)