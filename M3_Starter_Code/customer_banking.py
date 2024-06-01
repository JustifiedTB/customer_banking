# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance = input('Please enter the savings balance:  ')
    savings_interest = input('Please enter the savings interest rate:  ')
    savings_maturity = input('Please enter the savings maturity in months:  ')

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(f"The new balance is ${updated_savings_balance} after earning ${interest_earned} in interest.")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = input('Please enter the CD balance:  ')
    cd_interest = input('Please enter the CD interest rate:  ')
    cd_maturity = input('Please enter the CD maturity in months:  ')

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print(f"The new balance is ${updated_cd_balance} after earning ${interest_earned} in interest.")

if __name__ == "__main__":
    # Call the main function.
    main()