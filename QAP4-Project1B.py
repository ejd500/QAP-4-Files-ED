# Description: QAP 4 - Project 1B (Second Python Program)
# Author: Ellen Dalton
# Date: July 18, 2023

# Import required libraries
import matplotlib.pyplot as plt

# Main Program

while True:

    x_axis_lst = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    y_axis_lst = []

    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[0]}: "))
    y_axis_lst.append(sales_amt)
    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[1]}: "))
    y_axis_lst.append(sales_amt)
    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[2]}: "))
    y_axis_lst.append(sales_amt)
    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[3]}: "))
    y_axis_lst.append(sales_amt)
    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[4]}: "))
    y_axis_lst.append(sales_amt)
    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[5]}: "))
    y_axis_lst.append(sales_amt)
    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[6]}: "))
    y_axis_lst.append(sales_amt)
    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[7]}: "))
    y_axis_lst.append(sales_amt)
    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[8]}: "))
    y_axis_lst.append(sales_amt)
    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[9]}: "))
    y_axis_lst.append(sales_amt)
    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[10]}: "))
    y_axis_lst.append(sales_amt)
    sales_amt = float(input(f"Enter the total amount of sales for {x_axis_lst[11]}: "))
    y_axis_lst.append(sales_amt)

    # Create a bar chart
    plt.bar(x_axis_lst, y_axis_lst)

    # Plot labels and Title
    plt.title("QAP 4 - Python Program 2\n(Bar Chart)")
    plt.xlabel("Months")
    plt.ylabel("Total Sales ($)")

    # Show grid
    plt.grid(True)

    # Show the plot
    plt.show()

    print()

    Continue = input("Do you want to continue (Y/N)? ").upper()
    if Continue == "N":
        break
    else:
        continue
