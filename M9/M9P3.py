# Problem 3 - Miles per gallon with a function

def compute_mpg(miles, gallons):
    if gallons == 0:
        return 0.0
    return miles / gallons


trip_count = 0
response = "Y"

while response.upper() == "Y":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles travelled: "))
    gallons = float(input("Enter gallons used: "))

    mpg = compute_mpg(miles, gallons)
    trip_count += 1

    print(f"Destination: {city}  Miles: {miles:,.1f}  MPG: {mpg:.2f}")

    response = input("Enter another trip? (Y/N): ")

print(f"\nNumber of trips entered: {trip_count}")