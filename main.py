name_input = input("Enter name: ")
age_input = int(input("Enter age: "))

print(f"Hi my name is {name_input}. I am {age_input} years old.")

if age_input < 19:
    print("You're a Teenager")
else:
    print("You're an Adult")
