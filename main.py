import math as m
print("Enter X;Y target position:")
target = input().split(";")

angle = [0,0]
target[0] = float(target[0])
target[1] = float(target[1])

if target[0] > 0 and target[1] > 0:
    case = 1
elif target[0] > 0 and target[1] < 0:
    case = 2
    target[1] = target[1] * (-1)
elif target[0] < 0 and target[1] < 0:
    case = 3
    target[1] = target[1] * (-1)
    target[0] = target[0] * (-1)
elif target[0] < 0 and target[1] > 0:
    case = 4
    target[0] = target[0] * (-1)

distance = m.sqrt(target[0]**2 + target[1]**2)

if distance > 4:
    print("Out of range!")
    exit()

angle[0] = m.acos(distance**2/(4*distance))*180/m.pi
angle[1] = 180 - angle[0]*2
angle[0] = angle[0] + m.acos((distance**2+target[0]**2-target[1]**2)/(2*distance*target[0]))*180/m.pi

if case == 1:
    print("Both positive.")
elif case == 2:
    print("Y negative X positive")
    angle[0] = angle[0] * (-1)
    angle[1] = 360 - angle[1]
elif case == 3:
    print("Both negative")
    angle[0] = angle[0] * (-1) - 90
    angle[1] = 360 - angle[1]
elif case == 4:
    print("X negative Y positive")
    angle[0] = angle[0] + 90
print("Angle 1: " + str(angle[0]))
print("Angle 2: " + str(angle[1]))
