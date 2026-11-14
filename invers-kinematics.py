import numpy as np

# nim : 25/561250/TP/14515

input1 = input("Titik akhir x: ")
titikAkhir_x = float(input1)
input2 = input("Titik akhir y: ")
titikAkhir_y = float(input2)

a = 15
b = 50
c = np.sqrt((titikAkhir_x ** 2) + (titikAkhir_y ** 2))

sudut_C = np.rad2deg(np.arccos((a**2 + b**2 - c**2) / (2*a*b)))
sudut_q2 = round(180-sudut_C)

sudut_A = np.rad2deg(np.arccos((b**2 + c**2 - a**2) / (2*b*c)))
sudut_A_ke_sumbu_x = np.rad2deg(np.atan2(titikAkhir_y, titikAkhir_x))
sudut_q1 = round(sudut_A_ke_sumbu_x - sudut_A)

print(f"Sudut q1: {sudut_q1}°")
print(f"Sudut q2: {sudut_q2}°")
