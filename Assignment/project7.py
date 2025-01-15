# Week 7 assignment
import math

def calculate_wind_chill(temp,wind_speed):
    wci = 35.47 + 0.6215 * temp - 35.75 * (wind_speed ** 0.16) + 0.4275 * temp(wind_speed ** 0.16)
    return wci

temperature = input("What is the temperature? ")
choice = input ("Fahrenheit or Celsius (F/C)? ")
print()
for temp in range (5,10,15,20,25,30,35,40,45,50,55,60):
    print(temperature)