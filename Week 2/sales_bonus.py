"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    user_sales = float(input("Enter sales: $"))
    while user_sales >= 1:
        if user_sales < 1000:
            users_bonus = user_sales * 0.1
        else:
            users_bonus = user_sales * 0.15
        print(users_bonus)
        print("Try again!")
        user_sales = float(input("Enter sales: $"))
main()
