#!/usr/bin/env python3
"""
Comprehensive Python Tasks Menu System
A collection of various Python programming tasks and utilities
"""

import os
import sys
import json
import random
import string
import math
import datetime
from typing import List, Dict, Any
import re

class PythonTasksMenu:
    def __init__(self):
        self.tasks = []
        self.running = True
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def display_header(self):
        """Display the program header"""
        print("=" * 60)
        print("          COMPREHENSIVE PYTHON TASKS MENU")
        print("=" * 60)
        print()
        
    def display_main_menu(self):
        """Display the main menu options"""
        menu_options = [
            "1.  Basic Programming Tasks",
            "2.  String Operations",
            "3.  Data Structures & Algorithms",
            "4.  File Operations",
            "5.  Mathematical Operations",
            "6.  Date & Time Operations",
            "7.  Data Processing & Analysis",
            "8.  Games & Entertainment",
            "9.  Utility Tools",
            "10. Object-Oriented Programming Demo",
            "0.  Exit Program"
        ]
        
        for option in menu_options:
            print(option)
        print()
        
    def get_user_choice(self, max_choice: int) -> int:
        """Get and validate user choice"""
        while True:
            try:
                choice = int(input(f"Enter your choice (0-{max_choice}): "))
                if 0 <= choice <= max_choice:
                    return choice
                else:
                    print(f"Please enter a number between 0 and {max_choice}")
            except ValueError:
                print("Please enter a valid number")
                
    def pause(self):
        """Pause execution until user presses Enter"""
        input("\nPress Enter to continue...")
        
    # ===== BASIC PROGRAMMING TASKS =====
    def basic_programming_menu(self):
        """Basic programming tasks submenu"""
        while True:
            self.clear_screen()
            self.display_header()
            print("BASIC PROGRAMMING TASKS")
            print("-" * 30)
            print("1. Calculator")
            print("2. Number Guessing Game")
            print("3. FizzBuzz")
            print("4. Factorial Calculator")
            print("5. Prime Number Checker")
            print("6. Fibonacci Sequence")
            print("7. Temperature Converter")
            print("0. Back to Main Menu")
            print()
            
            choice = self.get_user_choice(7)
            
            if choice == 0:
                break
            elif choice == 1:
                self.calculator()
            elif choice == 2:
                self.number_guessing_game()
            elif choice == 3:
                self.fizzbuzz()
            elif choice == 4:
                self.factorial_calculator()
            elif choice == 5:
                self.prime_checker()
            elif choice == 6:
                self.fibonacci_sequence()
            elif choice == 7:
                self.temperature_converter()
                
    def calculator(self):
        """Basic calculator implementation"""
        print("\n=== CALCULATOR ===")
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            elif operator == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Error: Division by zero!")
                    self.pause()
                    return
            else:
                print("Invalid operator!")
                self.pause()
                return
                
            print(f"Result: {num1} {operator} {num2} = {result}")
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        
        self.pause()
        
    def number_guessing_game(self):
        """Number guessing game"""
        print("\n=== NUMBER GUESSING GAME ===")
        number = random.randint(1, 100)
        attempts = 0
        max_attempts = 7
        
        print(f"I'm thinking of a number between 1 and 100.")
        print(f"You have {max_attempts} attempts to guess it!")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
                attempts += 1
                
                if guess == number:
                    print(f"Congratulations! You guessed it in {attempts} attempts!")
                    break
                elif guess < number:
                    print("Too low!")
                else:
                    print("Too high!")
                    
                if attempts == max_attempts:
                    print(f"Game over! The number was {number}")
                    
            except ValueError:
                print("Please enter a valid number!")
                
        self.pause()
        
    def fizzbuzz(self):
        """FizzBuzz implementation"""
        print("\n=== FIZZBUZZ ===")
        try:
            limit = int(input("Enter the limit for FizzBuzz: "))
            
            for i in range(1, limit + 1):
                if i % 15 == 0:
                    print("FizzBuzz")
                elif i % 3 == 0:
                    print("Fizz")
                elif i % 5 == 0:
                    print("Buzz")
                else:
                    print(i)
                    
        except ValueError:
            print("Please enter a valid number!")
            
        self.pause()
        
    def factorial_calculator(self):
        """Calculate factorial of a number"""
        print("\n=== FACTORIAL CALCULATOR ===")
        try:
            n = int(input("Enter a number: "))
            if n < 0:
                print("Factorial is not defined for negative numbers!")
            else:
                factorial = 1
                for i in range(1, n + 1):
                    factorial *= i
                print(f"Factorial of {n} is {factorial}")
                
        except ValueError:
            print("Please enter a valid number!")
            
        self.pause()
        
    def prime_checker(self):
        """Check if a number is prime"""
        print("\n=== PRIME NUMBER CHECKER ===")
        try:
            n = int(input("Enter a number: "))
            
            if n < 2:
                print(f"{n} is not a prime number")
            else:
                is_prime = True
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        is_prime = False
                        break
                        
                if is_prime:
                    print(f"{n} is a prime number")
                else:
                    print(f"{n} is not a prime number")
                    
        except ValueError:
            print("Please enter a valid number!")
            
        self.pause()
        
    def fibonacci_sequence(self):
        """Generate Fibonacci sequence"""
        print("\n=== FIBONACCI SEQUENCE ===")
        try:
            n = int(input("Enter the number of terms: "))
            
            if n <= 0:
                print("Please enter a positive number!")
            else:
                a, b = 0, 1
                print(f"Fibonacci sequence with {n} terms:")
                
                for i in range(n):
                    if i == 0:
                        print(a, end=" ")
                    elif i == 1:
                        print(b, end=" ")
                    else:
                        c = a + b
                        print(c, end=" ")
                        a, b = b, c
                print()
                
        except ValueError:
            print("Please enter a valid number!")
            
        self.pause()
        
    def temperature_converter(self):
        """Convert temperature between Celsius and Fahrenheit"""
        print("\n=== TEMPERATURE CONVERTER ===")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        
        choice = self.get_user_choice(2)
        
        try:
            if choice == 1:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = (celsius * 9/5) + 32
                print(f"{celsius}°C = {fahrenheit}°F")
            elif choice == 2:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = (fahrenheit - 32) * 5/9
                print(f"{fahrenheit}°F = {celsius}°C")
                
        except ValueError:
            print("Please enter a valid number!")
            
        self.pause()
        
    # ===== STRING OPERATIONS =====
    def string_operations_menu(self):
        """String operations submenu"""
        while True:
            self.clear_screen()
            self.display_header()
            print("STRING OPERATIONS")
            print("-" * 20)
            print("1. String Analyzer")
            print("2. Palindrome Checker")
            print("3. Anagram Checker")
            print("4. Word Counter")
            print("5. String Reverser")
            print("6. Case Converter")
            print("7. Password Generator")
            print("0. Back to Main Menu")
            print()
            
            choice = self.get_user_choice(7)
            
            if choice == 0:
                break
            elif choice == 1:
                self.string_analyzer()
            elif choice == 2:
                self.palindrome_checker()
            elif choice == 3:
                self.anagram_checker()
            elif choice == 4:
                self.word_counter()
            elif choice == 5:
                self.string_reverser()
            elif choice == 6:
                self.case_converter()
            elif choice == 7:
                self.password_generator()
                
    def string_analyzer(self):
        """Analyze string properties"""
        print("\n=== STRING ANALYZER ===")
        text = input("Enter a string: ")
        
        print(f"\nAnalysis of: '{text}'")
        print(f"Length: {len(text)}")
        print(f"Characters: {len(text)}")
        print(f"Words: {len(text.split())}")
        print(f"Vowels: {sum(1 for c in text.lower() if c in 'aeiou')}")
        print(f"Consonants: {sum(1 for c in text.lower() if c.isalpha() and c not in 'aeiou')}")
        print(f"Digits: {sum(1 for c in text if c.isdigit())}")
        print(f"Spaces: {text.count(' ')}")
        print(f"Uppercase letters: {sum(1 for c in text if c.isupper())}")
        print(f"Lowercase letters: {sum(1 for c in text if c.islower())}")
        
        self.pause()
        
    def palindrome_checker(self):
        """Check if a string is palindrome"""
        print("\n=== PALINDROME CHECKER ===")
        text = input("Enter a string: ")
        
        # Remove spaces and convert to lowercase
        cleaned = ''.join(c.lower() for c in text if c.isalnum())
        
        if cleaned == cleaned[::-1]:
            print(f"'{text}' is a palindrome!")
        else:
            print(f"'{text}' is not a palindrome.")
            
        self.pause()
        
    def anagram_checker(self):
        """Check if two strings are anagrams"""
        print("\n=== ANAGRAM CHECKER ===")
        str1 = input("Enter first string: ")
        str2 = input("Enter second string: ")
        
        # Remove spaces and convert to lowercase
        clean1 = ''.join(c.lower() for c in str1 if c.isalnum())
        clean2 = ''.join(c.lower() for c in str2 if c.isalnum())
        
        if sorted(clean1) == sorted(clean2):
            print(f"'{str1}' and '{str2}' are anagrams!")
        else:
            print(f"'{str1}' and '{str2}' are not anagrams.")
            
        self.pause()
        
    def word_counter(self):
        """Count words in a text"""
        print("\n=== WORD COUNTER ===")
        text = input("Enter a text: ")
        
        words = text.split()
        word_count = {}
        
        for word in words:
            clean_word = ''.join(c.lower() for c in word if c.isalnum())
            if clean_word:
                word_count[clean_word] = word_count.get(clean_word, 0) + 1
                
        print(f"\nTotal words: {len(words)}")
        print(f"Unique words: {len(word_count)}")
        print("\nWord frequencies:")
        
        for word, count in sorted(word_count.items()):
            print(f"{word}: {count}")
            
        self.pause()
        
    def string_reverser(self):
        """Reverse a string"""
        print("\n=== STRING REVERSER ===")
        text = input("Enter a string: ")
        
        print(f"Original: {text}")
        print(f"Reversed: {text[::-1]}")
        
        self.pause()
        
    def case_converter(self):
        """Convert string case"""
        print("\n=== CASE CONVERTER ===")
        text = input("Enter a string: ")
        
        print(f"Original: {text}")
        print(f"Uppercase: {text.upper()}")
        print(f"Lowercase: {text.lower()}")
        print(f"Title Case: {text.title()}")
        print(f"Capitalize: {text.capitalize()}")
        print(f"Swapcase: {text.swapcase()}")
        
        self.pause()
        
    def password_generator(self):
        """Generate random password"""
        print("\n=== PASSWORD GENERATOR ===")
        
        try:
            length = int(input("Enter password length (8-50): "))
            if length < 8 or length > 50:
                print("Password length should be between 8 and 50!")
                self.pause()
                return
                
            include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
            include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
            include_digits = input("Include digits? (y/n): ").lower() == 'y'
            include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
            
            chars = ""
            if include_uppercase:
                chars += string.ascii_uppercase
            if include_lowercase:
                chars += string.ascii_lowercase
            if include_digits:
                chars += string.digits
            if include_symbols:
                chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
                
            if not chars:
                print("You must select at least one character type!")
                self.pause()
                return
                
            password = ''.join(random.choice(chars) for _ in range(length))
            print(f"Generated password: {password}")
            
        except ValueError:
            print("Please enter a valid number!")
            
        self.pause()
        
    # ===== MATHEMATICAL OPERATIONS =====
    def mathematical_operations_menu(self):
        """Mathematical operations submenu"""
        while True:
            self.clear_screen()
            self.display_header()
            print("MATHEMATICAL OPERATIONS")
            print("-" * 25)
            print("1. Area Calculator")
            print("2. Number System Converter")
            print("3. Matrix Operations")
            print("4. Statistical Calculator")
            print("5. Equation Solver")
            print("0. Back to Main Menu")
            print()
            
            choice = self.get_user_choice(5)
            
            if choice == 0:
                break
            elif choice == 1:
                self.area_calculator()
            elif choice == 2:
                self.number_system_converter()
            elif choice == 3:
                self.matrix_operations()
            elif choice == 4:
                self.statistical_calculator()
            elif choice == 5:
                self.equation_solver()
                
    def area_calculator(self):
        """Calculate area of different shapes"""
        print("\n=== AREA CALCULATOR ===")
        print("1. Circle")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Square")
        
        shape = self.get_user_choice(4)
        
        try:
            if shape == 1:
                radius = float(input("Enter radius: "))
                area = math.pi * radius ** 2
                print(f"Area of circle: {area:.2f}")
            elif shape == 2:
                length = float(input("Enter length: "))
                width = float(input("Enter width: "))
                area = length * width
                print(f"Area of rectangle: {area:.2f}")
            elif shape == 3:
                base = float(input("Enter base: "))
                height = float(input("Enter height: "))
                area = 0.5 * base * height
                print(f"Area of triangle: {area:.2f}")
            elif shape == 4:
                side = float(input("Enter side length: "))
                area = side ** 2
                print(f"Area of square: {area:.2f}")
                
        except ValueError:
            print("Please enter valid numbers!")
            
        self.pause()
        
    def number_system_converter(self):
        """Convert between number systems"""
        print("\n=== NUMBER SYSTEM CONVERTER ===")
        print("1. Decimal to Binary")
        print("2. Decimal to Hexadecimal")
        print("3. Binary to Decimal")
        print("4. Hexadecimal to Decimal")
        
        choice = self.get_user_choice(4)
        
        try:
            if choice == 1:
                num = int(input("Enter decimal number: "))
                print(f"Binary: {bin(num)[2:]}")
            elif choice == 2:
                num = int(input("Enter decimal number: "))
                print(f"Hexadecimal: {hex(num)[2:].upper()}")
            elif choice == 3:
                num = input("Enter binary number: ")
                decimal = int(num, 2)
                print(f"Decimal: {decimal}")
            elif choice == 4:
                num = input("Enter hexadecimal number: ")
                decimal = int(num, 16)
                print(f"Decimal: {decimal}")
                
        except ValueError:
            print("Please enter a valid number!")
            
        self.pause()
        
    def matrix_operations(self):
        """Basic matrix operations"""
        print("\n=== MATRIX OPERATIONS ===")
        print("Creating 2x2 matrices for demonstration")
        
        try:
            print("Enter first matrix:")
            matrix1 = []
            for i in range(2):
                row = []
                for j in range(2):
                    val = float(input(f"Enter element [{i+1}][{j+1}]: "))
                    row.append(val)
                matrix1.append(row)
                
            print("Enter second matrix:")
            matrix2 = []
            for i in range(2):
                row = []
                for j in range(2):
                    val = float(input(f"Enter element [{i+1}][{j+1}]: "))
                    row.append(val)
                matrix2.append(row)
                
            # Addition
            result_add = [[matrix1[i][j] + matrix2[i][j] for j in range(2)] for i in range(2)]
            print("\nMatrix Addition:")
            for row in result_add:
                print(row)
                
            # Subtraction
            result_sub = [[matrix1[i][j] - matrix2[i][j] for j in range(2)] for i in range(2)]
            print("\nMatrix Subtraction:")
            for row in result_sub:
                print(row)
                
            # Multiplication
            result_mul = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
            print("\nMatrix Multiplication:")
            for row in result_mul:
                print(row)
                
        except ValueError:
            print("Please enter valid numbers!")
            
        self.pause()
        
    def statistical_calculator(self):
        """Calculate basic statistics"""
        print("\n=== STATISTICAL CALCULATOR ===")
        
        numbers_input = input("Enter numbers separated by spaces: ")
        try:
            numbers = [float(x) for x in numbers_input.split()]
            
            if not numbers:
                print("No numbers entered!")
                self.pause()
                return
                
            # Calculate statistics
            mean = sum(numbers) / len(numbers)
            numbers_sorted = sorted(numbers)
            n = len(numbers)
            
            # Median
            if n % 2 == 0:
                median = (numbers_sorted[n//2 - 1] + numbers_sorted[n//2]) / 2
            else:
                median = numbers_sorted[n//2]
                
            # Mode
            from collections import Counter
            counts = Counter(numbers)
            max_count = max(counts.values())
            mode = [k for k, v in counts.items() if v == max_count]
            
            # Range
            range_val = max(numbers) - min(numbers)
            
            # Standard deviation
            variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
            std_dev = math.sqrt(variance)
            
            print(f"\nStatistics for {len(numbers)} numbers:")
            print(f"Mean: {mean:.2f}")
            print(f"Median: {median:.2f}")
            print(f"Mode: {mode}")
            print(f"Range: {range_val:.2f}")
            print(f"Standard Deviation: {std_dev:.2f}")
            print(f"Minimum: {min(numbers):.2f}")
            print(f"Maximum: {max(numbers):.2f}")
            
        except ValueError:
            print("Please enter valid numbers!")
            
        self.pause()
        
    def equation_solver(self):
        """Solve quadratic equations"""
        print("\n=== QUADRATIC EQUATION SOLVER ===")
        print("Solving ax² + bx + c = 0")
        
        try:
            a = float(input("Enter coefficient a: "))
            b = float(input("Enter coefficient b: "))
            c = float(input("Enter coefficient c: "))
            
            if a == 0:
                print("Not a quadratic equation (a cannot be 0)")
                self.pause()
                return
                
            discriminant = b**2 - 4*a*c
            
            if discriminant > 0:
                x1 = (-b + math.sqrt(discriminant)) / (2*a)
                x2 = (-b - math.sqrt(discriminant)) / (2*a)
                print(f"Two real solutions: x1 = {x1:.2f}, x2 = {x2:.2f}")
            elif discriminant == 0:
                x = -b / (2*a)
                print(f"One real solution: x = {x:.2f}")
            else:
                real_part = -b / (2*a)
                imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
                print(f"Complex solutions:")
                print(f"x1 = {real_part:.2f} + {imaginary_part:.2f}i")
                print(f"x2 = {real_part:.2f} - {imaginary_part:.2f}i")
                
        except ValueError:
            print("Please enter valid numbers!")
            
        self.pause()
        
    # ===== MAIN EXECUTION =====
    def run(self):
        """Main program loop"""
        while self.running:
            self.clear_screen()
            self.display_header()
            self.display_main_menu()
            
            choice = self.get_user_choice(10)
            
            if choice == 0:
                self.running = False
                print("Thank you for using the Python Tasks Menu!")
            elif choice == 1:
                self.basic_programming_menu()
            elif choice == 2:
                self.string_operations_menu()
            elif choice == 3:
                print("Data Structures & Algorithms - Coming Soon!")
                self.pause()
            elif choice == 4:
                print("File Operations - Coming Soon!")
                self.pause()
            elif choice == 5:
                self.mathematical_operations_menu()
            elif choice == 6:
                print("Date & Time Operations - Coming Soon!")
                self.pause()
            elif choice == 7:
                print("Data Processing & Analysis - Coming Soon!")
                self.pause()
            elif choice == 8:
                print("Games & Entertainment - Coming Soon!")
                self.pause()
            elif choice == 9:
                print("Utility Tools - Coming Soon!")
                self.pause()
            elif choice == 10:
                print("Object-Oriented Programming Demo - Coming Soon!")
                self.pause()

def main():
    """Main function to run the program"""
    menu = PythonTasksMenu()
    menu.run()

if __name__ == "__main__":
    main()
