def bmi_calculator(height, weight):
    height = int(height) / 100 
    bmi = weight / (height * height)
    print(f"Your BMI is {bmi:.2f}")

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25.0 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"BMI Category: {category}")

height = int(input("Your Height in cm is: "))
weight = int(input("Your Weight in kg is: "))

bmi_calculator(height, weight)
