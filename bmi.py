def calculate_bmi(weight, height):
    # Calculate BMI
    bmi = weight / (height ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    # Categorize the BMI
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")

    # Input validation for weight
    while True:
        try:
            weight = float(input("Enter your weight in kilograms: "))
            if weight <= 0:
                raise ValueError("Weight must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    # Input validation for height
    while True:
        try:
            height = float(input("Enter your height in meters: "))
            if height <= 0:
                raise ValueError("Height must be a positive number.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    # Calculate and classify BMI
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)

    # Display the result
    print(f"\nYour BMI is {bmi}. You are classified as {category}.")

if __name__ == "__main__":
    main()
