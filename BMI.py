#Do not CopyRight
#PA

print("Calculator BMI")
print("-----------------------------")
print("Write your Wight{Kg} and Hight{Cm}")
Kg = int(input("Kg==>"))
CM = int(input("Cm==>"))
CMtoM = CM / 100
BMI = Kg // (CMtoM**2)
print(BMI)
if BMI<18.5:
    print("Thin")
if 24.5>BMI>18.5:
    print("Normal")
if 29.9>BMI>24.5:
    print("Fat")
if BMI>30:
    print("Very Fat")
print("-----------------------------")
print("Creator :PA")