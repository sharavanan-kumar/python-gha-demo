import numpy as np

def calculate_correlation(x, y):
    """Calculates the Pearson correlation coefficient between two arrays."""
    return np.corrcoef(x, y)[0, 1]

if __name__ == "__main__":
    try:
        x_str = input("Enter the first number: ")
        y_str = input("Enter the second number: ")

        x = float(x_str)
        y = float(y_str)

        correlation = calculate_correlation([x], [y])
        print(f"The correlation between {x} and {y} is: {correlation}")

    except ValueError:
        print("Invalid input. Please enter numbers.")
    except Exception as e:
        print(f"An error occurred: {e}")
