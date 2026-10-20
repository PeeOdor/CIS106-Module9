# Problem 4 - Pay rate by job code with a function

def get_pay_rate(job_code):
    if job_code == "L":
        return 25.0
    elif job_code == "A":
        return 30.0
    elif job_code == "J":
        return 50.0
    else:
        return 0.0


total_gross = 0.0
response = "Y"

while response.upper() == "Y":
    last_name = input("Enter employee last name: ")
    job_code = input("Enter job code (L, A, J): ").upper()
    hours = float(input("Enter hours worked: "))

    rate = get_pay_rate(job_code)

    if hours > 40:
        gross_pay = (40 * rate) + ((hours - 40) * rate * 1.5)   # time and a half
    else:
        gross_pay = hours * rate

    total_gross += gross_pay

    print(f"Employee: {last_name}  Gross Pay: ${gross_pay:,.2f}")

    response = input("Enter another employee? (Y/N): ")

print(f"\nTotal gross pay for all employees: ${total_gross:,.2f}")