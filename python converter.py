def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def miles_to_km(miles):
    return miles * 1.60934

def km_to_miles(km):
    return km / 1.60934

def main():
    print("--- Multi-Tool Unit Converter ---")
    
    while True:
        print("\nSelect a conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Miles to Kilometers")
        print("4. Kilometers to Miles")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice in ["1", "2", "3", "4"]:
            try:
                val = float(input("Enter value to convert: "))
            except ValueError:
                print("❌ Invalid
