import math

def rad(x):
    return x * 180 / math.pi


while True:
    print("Radians to Degrees converter")
    print("")
    print("Type [P] to proceed to the conversion")
    print("Type [E] to exit the program")
    user_input = input(" :")

    if user_input == 'E':
        print("PROGRAM TERMINATED")
        break
    elif user_input == 'P':
        num1 = float(input("Enter a Radian :"))
        print("Radian is = ", rad(num1, ))
