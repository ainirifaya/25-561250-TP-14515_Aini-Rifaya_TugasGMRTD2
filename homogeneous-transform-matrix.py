import numpy as np

#nim: 25/561250/TP/14515

input_x = input("Masukkan koordinat awal coxa x: ")
tp_x = float(input_x)
input_y = input("Masukkan koordinat awal coxa y: ")
tp_y = float(input_y)
input1 = input("Masukkan derajat servo 1: ")
sudut_servo1 = float(input1)
input2 = input("Masukkan derajat servo 2: ")
sudut_servo2 = float(input2)
total_sudut = sudut_servo1 + sudut_servo2

cos1 = np.cos(np.deg2rad(sudut_servo1))
koordinatx1 = (50 * np.cos(np.deg2rad(sudut_servo1))) + tp_x
sin1 = np.sin(np.deg2rad(sudut_servo1))
koordinaty1 = (50 * np.sin(np.deg2rad(sudut_servo1))) + tp_y
cos2 = np.cos(np.deg2rad(total_sudut))
koordinatx2 = (15 * np.cos(np.deg2rad(total_sudut))) + koordinatx1
sin2 = np.sin(np.deg2rad(total_sudut))
koordinaty2 = (15 * np.sin(np.deg2rad(total_sudut))) + koordinaty1

matriks_femur = np.array([
  [cos1, -(sin1), koordinatx1],
  [sin1, cos1, koordinaty1],
  [0, 0, 1]
])
koordinat_x1 = matriks_femur[0, 2]
koordinat_y1 = matriks_femur[1, 2]

matriks_tibia = np.array([
  [cos2, -(sin2), koordinatx2],
  [sin2, cos2, koordinaty2],
  [0, 0, 1]
])
koordinat_x2 = matriks_tibia[0, 2]
koordinat_y2 = matriks_tibia[1, 2]

print("Matriks femur: ")
print(matriks_femur)
print(f"Koordinat di ujung Femur: [ {koordinat_x1:.4f}, {koordinat_y1:.4f} ]")
print(" ")

print("Matriks tibia: ")
print(matriks_tibia)
print(f"Koordinat di ujung Tibia: [ {koordinat_x2:.4f}, {koordinat_y2:.4f} ]")
