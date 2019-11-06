import sys

from datetime import datetime

print("******====== 01 ======******")
print("""twinkle, twinkle, little star,
        how i wonder what you are!
              up above the world so high,
              Like a diamond in the sky.
twinkle ,twinkle ,little star,
        how i wonder what you are""")

print("******====== 02 ======******")

print("Python version")
print(sys.version)

now = datetime.now()

print("now =", now)
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time = ", dt_string)

print("******====== 03 ======******")

rad = input("input radius : ")
area = 3.142 * float(rad) * float(rad)
print("area of the circle for the given radius is : " + str(area))

print("******====== 04 ======*******")


first_name = input("enter first name: ")
last_name = input("enter last name: ")
full_name = first_name + " " + last_name
print(full_name)
reversed = ''.join(reversed(full_name))
print(reversed)

print("*******======= 05 =======*******")

a = int(input())
b = int(input())
print(a + b)

