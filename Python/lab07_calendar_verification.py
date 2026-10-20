#Calendar Verification System
print("       CALENDAR VERIFICATION SYSTEM              ")
year = int(input("Enter year: "))
if year <= 0:
    print("Error: Year must be a positive integer.")
else:
    if year % 400 == 0:
        status = "LEAP YEAR"
        reason = "Century year divisible by 400"
    elif year % 100 == 0:
        status = "COMMON YEAR"
        reason = "Century year not divisible by 400"
    elif year % 4 == 0:
        status = "LEAP YEAR"
        reason = "Divisible by 4 and not a century year"
    else:
        status = "COMMON YEAR"
        reason = "Not divisible by 4"
    if status == "LEAP YEAR":
        total_days = 366
        february_days = 29
    else:
        total_days = 365
        february_days = 28
    print(f"Year: {year}")
    print(f"Status: {status}")
    print(f"Days in Year: {total_days} days")
    print(f"Days in February: {february_days} days")
    print(f"Reason: {reason}")