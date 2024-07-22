def compute_bmi(weight_kg, height_m):
    """Computing the Body Mass Index (BMI) using weight in kg and height in meters."""
    return weight_kg / (height_m ** 2)

def categorize_bmi(bmi_value):
    """Determining the BMI category based on the BMI value."""
    if bmi_value < 18.5:
        return "Underweight"
    elif 18.5 <= bmi_value < 24.9:
        return "Normal weight"
    elif 25 <= bmi_value < 29.9:
        return "Overweight"
    elif 30 <= bmi_value < 34.9:
        return "Obesity Class I"
    elif 35 <= bmi_value < 39.9:
        return "Obesity Class II"
    else:
        return "Obesity Class III"

def get_user_input():
    """Prompting the user to input their weight and height, and handling invalid inputs."""
    while True:
        try:
            weight_kg = float(input("Please enter your weight in kilograms: "))
            height_m = float(input("Please enter your height in meters: "))
            return weight_kg, height_m
        except ValueError:
            print("Invalid input. Please enter numeric values.")

def display_bmi_result(bmi_value, bmi_category):
    """Displaying the BMI result and its category."""
    print(f"Your BMI is: {bmi_value:.2f}")
    print(f"You are classified as: {bmi_category}")

def main():
    """Main function to run the BMI calculator."""
    weight_kg, height_m = get_user_input()
    bmi_value = compute_bmi(weight_kg, height_m)
    bmi_category = categorize_bmi(bmi_value)
    display_bmi_result(bmi_value, bmi_category)

if __name__ == "__main__":
    main()
