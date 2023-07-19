# Description: QAP 4 - Project 1B (Second Python Program)
# Author: Ellen Dalton
# Date: July 18, 2023

# Import required libraries
import matplotlib.pyplot as plt

# Main Program

while True:

    x_axis_lst = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sept", "Oct", "Nov", "Dec"]
    y_axis_lst = []

    for i in x_axis_lst:
        sales_amt = float(input(f"Enter the total sales for {i}: "))
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
