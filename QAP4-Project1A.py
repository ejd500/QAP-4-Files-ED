# Description: QAP 4 - Project 1A
# Author: Ellen Dalton
# Date: July 17, 2023

# Import required libraries
import datetime
curr_date = datetime.datetime.now()
from tqdm import tqdm
import time

# Open the defaults file and read the values into variables

f = open('OSICDef.dat', 'r')

NEXT_POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
COST_EXTRA_LIABILITY = float(f.readline())
COST_GLASS_COVERAGE = float(f.readline())
COST_LOANER_COVERAGE = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())

f.close()

# Define Required Functions

# Main Program
while True:
    
    # Inputs:
    
    first_name = input("Enter the customer's first name: ").title()
    
    last_name = input("Enter the customer's last name: ").title()
    
    address = input("Enter the address: ").title()
    
    city = input("Enter the city: ").title()
    
    prov_lst = ["NL", "NS", "PE", "NB", "QB", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
    while True:
        province = input("Enter the province (LL): ").upper()
        if province == "":
            print("Error - Province cannot be blank. Please re-enter.")
        elif len(province) != 2:
            print("Error - Province must be 2 letters only. Please re-enter.")
        elif province not in prov_lst:
            print("Error - Not a valid province. Please re-enter.")
        else:
            break
    
    postal_code = input("Enter the postal code (A1A2B2): ").upper()
    
    phone_num = input("Enter the phone number (9999999999): ")
    
    num_cars_insured = int(input("Enter the number of cars being insured (must be 1 or greater): "))
    
    extra_liability = input("Do you want extra liability up to $1,000,000 (Y for Yes or N for No)? ").upper()
    
    glass_coverage = input("Do you want glass coverage (Y for Yes or N for No)? ").upper()
    
    loaner_car = input("Do you want a loaner car (Y for Yes or N for No)? ").upper()
    
    payment_option_lst = ["Full", "Monthly"]
    while True:
        payment_option = input("Do you want to pay in full or monthly (Full or Monthly)? ").title()
        if payment_option == "":
            print("Error - Payment option cannot be blank. Please re-enter.")
        elif payment_option not in payment_option_lst:
            print("Error - Payment option is not a valid option. Please re-enter.")
        else:
            break
    
    # Calculations:
    
    if num_cars_insured == 1:
        insurance_premium = BASIC_PREMIUM
    elif num_cars_insured > 1:
        insurance_premium = BASIC_PREMIUM + ADD_CAR_DISCOUNT * (num_cars_insured - 1)
    
    if extra_liability == "Y":
        cost_extra_liability = COST_EXTRA_LIABILITY * num_cars_insured
    elif extra_liability == "N":
        cost_extra_liability = 0
    
    if glass_coverage == "Y":
        cost_glass_coverage = COST_GLASS_COVERAGE * num_cars_insured
    elif glass_coverage == "N":
        cost_glass_coverage = 0
    
    if loaner_car == "Y":
        cost_loaner_car = COST_LOANER_COVERAGE * num_cars_insured
    elif loaner_car == "N":
        cost_loaner_car = 0
        
    total_extra_costs = cost_extra_liability + cost_glass_coverage + cost_loaner_car
    
    total_insurance_premium = insurance_premium + total_extra_costs
    
    hst = HST_RATE * total_insurance_premium
    
    total_cost = total_insurance_premium + hst
    
    if payment_option == "Monthly":
        monthly_payment = (total_cost + PROCESSING_FEE)/8

    invoice_date = curr_date.strftime("%Y-%m-%d")

    invoice_year = curr_date.year
    invoice_month = curr_date.month

    if invoice_month == 12:
        next_payment_date = str(invoice_year + 1) + "-" + "01" + "-" + "01"
    elif invoice_month == 1:
        next_payment_date = str(invoice_year) + "-" + "0" + str(invoice_month + 1) + "-" + "01"
    elif invoice_month == 2:
        next_payment_date = str(invoice_year) + "-" + "0" + str(invoice_month + 1) + "-" + "01"
    elif invoice_month == 3:
        next_payment_date = str(invoice_year) + "-" + "0" + str(invoice_month + 1) + "-" + "01"
    elif invoice_month == 4:
        next_payment_date = str(invoice_year) + "-" + "0" + str(invoice_month + 1) + "-" + "01"
    elif invoice_month == 5:
        next_payment_date = str(invoice_year) + "-" + "0" + str(invoice_month + 1) + "-" + "01"
    elif invoice_month == 6:
        next_payment_date = str(invoice_year) + "-" + "0" + str(invoice_month + 1) + "-" + "01"
    elif invoice_month == 7:
        next_payment_date = str(invoice_year) + "-" + "0" + str(invoice_month + 1) + "-" + "01"
    elif invoice_month == 8:
        next_payment_date = str(invoice_year) + "-" + "0" + str(invoice_month + 1) + "-" + "01"
    else:
        next_payment_date = str(invoice_year) + "-" + str(invoice_month + 1) + "-" + "01"

    # Output

    print()
    print(f"---------------------------------------------------------")
    print("                One Stop Insurance Company")
    print(f"---------------------------------------------------------")
    print()
    full_name = first_name + " " + last_name
    print(f"Customer: {full_name:<22s} Invoice Date: {invoice_date}")
    print()
    print(f"Address:  {address:<22s} Phone Number: {phone_num:>10s}")
    city_prov = city + ", " + province
    print(f"          {city_prov:<27s}")
    print(f"          {postal_code:<6s}")
    print()
    print(f"Cars Insured: {num_cars_insured:>5d}       Insurance Premium:    ${insurance_premium:>8.2f}")
    print(f"Extra Liability: {extra_liability:>2s}       Extra Liability Cost: ${cost_extra_liability:>8.2f}")
    print(f"Glass Coverage: {glass_coverage:>3s}       Glass Coverage Cost:  ${cost_glass_coverage:>8.2f}")
    print(f"Loaner Car:     {loaner_car:>3s}       Loaner Car Cost:      ${cost_loaner_car:>8.2f}")
    print(f"                          -------------------------------")
    print(f"                          Total Extra Costs:    ${total_extra_costs:>8.2f}")
    print()
    print(f"                          Subtotal:             ${total_insurance_premium:>8.2f}")
    print(f"                          HST:                  ${hst:>8.2f}")
    print(f"                          -------------------------------")
    print(f"                          Total:                ${total_cost:>8.2f}")
    print(f"                          -------------------------------")
    print(f"                          Payment Option:         {payment_option:>7s}")
    if payment_option == "Monthly":
        print(f"                          Monthly Payment:      ${monthly_payment:>8.2f}")
    print(f"                          Next Payment Date:   {next_payment_date:>10s}")
    print(f"---------------------------------------------------------")
    print(f"                     Thank you!")
    print(f"---------------------------------------------------------")
    print()

    # Save the policy number, all input values and the total insurance premium to a file called Policies.dat

    f = open("Policies.dat", "a")

    f.write(f"{NEXT_POLICY_NUM}, ")
    f.write(f"{invoice_date}, ")
    f.write(f"{first_name}, ")
    f.write(f"{last_name}, ")
    f.write(f"{address}, ")
    f.write(f"{city}, ")
    f.write(f"{province}, ")
    f.write(f"{postal_code}, ")
    f.write(f"{phone_num}, ")
    f.write(f"{num_cars_insured}, ")
    f.write(f"{extra_liability}, ")
    f.write(f"{glass_coverage}, ")
    f.write(f"{loaner_car}, ")
    f.write(f"{payment_option}, ")
    f.write(f"{total_insurance_premium:>.2f}\n")

    f.close()

    # Create a progress bar...
    # Define the total number of iterations
    total_iterations = 100

    # Create a loop and wrap it with tqdm
    for i in tqdm(range(total_iterations), bar_format="{desc}: Saving in progress: {bar} {percentage:3.0f}%", ncols=57):
        # Simulate some work
        time.sleep(0.03)
    print()
    print("Policy information processed and saved.")
    print()

    NEXT_POLICY_NUM += 1

    Continue = input("Do you want to enter and calculate another insurance policy (Y or N)? ").upper()
    if Continue == "N":
        break
    else:
        continue

# Write the current values back to the defaults file.
f = open('OSICDef.dat', 'w')

f.write(f"{NEXT_POLICY_NUM}\n")
f.write(f"{BASIC_PREMIUM}\n")
f.write(f"{ADD_CAR_DISCOUNT}\n")
f.write(f"{COST_EXTRA_LIABILITY}\n")
f.write(f"{COST_GLASS_COVERAGE}\n")
f.write(f"{COST_LOANER_COVERAGE}\n")
f.write(f"{HST_RATE}\n")
f.write(f"{PROCESSING_FEE}\n")

f.close()
