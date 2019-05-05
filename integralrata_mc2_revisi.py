# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:46:08 2019

@author: Febiana Anistya
"""

#TUBES DASAR PEMODELAN DAN SIMULASI
#   Materi     : Menghitung Integral Lipat Satu (nilai rata-rata)
#   Kelompok   : Nomor 5    
#   Kelas      : IF 40 03
#   Anggota    : Febiana Anistya
#                Maya Ameliasari

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import random as rand

# Kami ambil nilai seperti request Bapak saat presentasi kemarin
# Fungsi yang diambil x^2
def f(x):
    return (x**2)

n = 100     #titik yang dibangkitkan
a = 0       #batas bawah
b = 3       #batas atas

S = 0
S2 = 0
# Langkah 1
for i in range(n):
    r = rand.uniform(0,1)
    xr = a + ((b - a) * r)
    S = S + f(xr)
    S2 = S2 + (f(xr) * f(xr))
#endfor
    
# Langkah 2
Favg = S/n
F2avg = S2/n
# Langkah 3
Fn = (b - a) * Favg
pe = (b - a) * math.sqrt((F2avg - (Favg*Favg)) / n)

# Grafik
x = np.linspace(0, 5)
y = f(x)
fig, ax = plt.subplots()
plt.plot(x, y)
plt.ylim(0)

# Buat area grafiknya
ix = np.linspace(a, b)
iy = f(ix)
verts = [(a, 0), *zip(ix, iy), (b, 0)]
polygon = Polygon(verts, facecolor='#41f4af', edgecolor='red')
ax.add_patch(polygon)
plt.show()

#Output
print('Fungsi = x^2')
print('Banyak titik yang dibangkitkan (n) = ',n)
print()
print('Hasil Langkah 1')
print('=======================')
print('S   : ',round(S,4))
print('S2  : ',round(S2,4))
print()
print('Hasil Langkah 2')
print('=======================')
print('Favg   : ',round(Favg,4))
print('F2avg  : ',round(F2avg,4))
print()
print('Hasil Langkah 3')
print('=======================')
print('Fn     : ',round(Fn,4)) # Hasil integral numerik
print('pe     : ',round(pe,4)) # Perkiraan error
