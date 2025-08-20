#!/usr/bin/env python3

def admin_login(username, password):
    # Check if username is "admin" or "ADMIN" and password is "12345"
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"


def hows_the_weather(temperature):
    # Return different responses based on temperature
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    # Multiples of 3 and 5
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    # Multiples of 3
    elif num % 3 == 0:
        return "Fizz"
    # Multiples of 5
    elif num % 5 == 0:
        return "Buzz"
    # Otherwise return the number
    else:
        return num


def calculator(operation, num1, num2):
    # Perform arithmetic based on operation
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
