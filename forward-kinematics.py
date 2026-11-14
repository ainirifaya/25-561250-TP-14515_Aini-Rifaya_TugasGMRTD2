import numpy as np

#nim: 25/561250/TP/14515

input1 = input("Masukkan derajat servo 1: ")
sudut_servo1 = float(input1)
x1 = 50 * np.cos(np.deg2rad(sudut_servo1))
y1 = 50 * np.sin(np.deg2rad(sudut_servo1))

koordinat1 = np.array([x1, y1])
print("Koordinat di ujung Femur: ", koordinat1)

input2 = input("Masukkan derajat servo 2: ")
sudut_servo2 = float(input2)
x2 = (15 * np.cos(np.deg2rad(sudut_servo1 + sudut_servo2))) + x1
y2 = (15 * np.sin(np.deg2rad(sudut_servo1 + sudut_servo2))) + y1

koordinat2 = np.array([x2, y2])
print("Koordinat di ujung Tibia: ", koordinat2)
