# Problem 5 - Tuition owed with a function

def compute_tuition(credit_hours, district_code):
    if district_code == "I":
        return credit_hours * 250.0
    elif district_code == "O":
        return credit_hours * 550.0
    else:
        return 0.0


total_tuition = 0.0
response = "Y"

while response.upper() == "Y":
    last_name = input("Enter student last name: ")
    credit_hours = int(input("Enter credit hours: "))
    district_code = input("Enter district code (I = in district, O = out of district): ").upper()

    tuition = compute_tuition(credit_hours, district_code)
    total_tuition += tuition

    print(f"Student: {last_name}  Tuition Owed: ${tuition:,.2f}")

    response = input("Enter another student? (Y/N): ")

print(f"\nTotal tuition owed for all students: ${total_tuition:,.2f}")