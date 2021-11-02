# Fanny Devita Inggarini (1194015-D4TI3A)
# 1194015 mod 8 = 7. Maka saya membuat segitiga siku siku sebanyak 1 buah (n adalah digit kedua terakhir dari npm, karena angka kedua terakhir dari npm saya adalah 1 jadi membuat satu)

import shapefile

w=shapefile.Writer("soal10",shapeType=shapefile.POLYGON)
w.shapeType

w.field("kolom1","C")
w.field("kolom2","C")

w.record("cetar","satu")


w.poly([[[-8,5], [-8,-1], [3,-1]]])


w.close()