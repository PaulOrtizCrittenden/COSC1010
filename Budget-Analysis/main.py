#
# Paul Ortiz
# 3/2/25
# Budget Analysis Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Establish an accumulator variable
totalExpense = 0

# Establish an input for budget
budget = float(input('Input budget for this month: $'))
budget = round(budget, 2)

# Test
# Good so far

# Begin inputting expenses and keeping a running tally

while True:
    expense = input("Enter an expense amount (type 'done' if finished): ")

    #input a break string so that that program knows to stop tallying
    if expense.lower() == 'done' :
        break

    # get the running tally to work, adding expenses input to a running total

    try: 
        expense = float(expense)
        totalExpense += expense

    # because we have numerical inputs and letters, we need to make sure people only put in the correct inputs

    except ValueError: 
        print("Invalid input. Please enter a numerical expense or 'done' to finish")
    
    #display remaining budget and running total expenses
    remainingBudget = budget - totalExpense
    print(f"Total Expenses: $ {totalExpense: .2f} ")
    print(f"Remaining Budget: $ {remainingBudget: .2f} ")

   # Throw in a warning if someone is going over budget before they're done bcause that's how I actually do my budgets in real life
    from colorama import Fore, Style

    if remainingBudget < 0:
        print(Fore.RED + 'Warning: You have exceeded your established budget!' + Style.RESET_ALL)

# Test progress so far   
# A little bit more work to do here



if totalExpense > budget:
    
    print('Budget Summary ')
    print( f"Initial Budget: ${budget: .2f} ")
    print( f"Total Expenses: ${totalExpense: .2f} ")
    print(f"Over budget by:  ${abs(remainingBudget): .2f} ") 
    print( Fore.RED + 'You have gone over budget!' + Style.RESET_ALL )

else:
    
    print('Budget Summary ')
    print( f"Initial Budget: ${budget: .2f} ")
    print( f"Total Expenses: ${totalExpense: .2f} ")
    print(f"Remaining Budget: ${remainingBudget: .2f} ")
    print( Fore.GREEN + 'You are within your budget, good work!' + Style.RESET_ALL )
# let's test this now
# test success, but I have to tweak the colors I was using
# another successful test, but then I realized that it was displaying remaining budget as a negative number, even if i went over budget
# to correct this, I changed the if statement to print two diffierent outputs depending on whether someone was over or under budget
# over budget will now show an "Over budget: $" with an absolute value to the remainingBudget variable
# within budget will show a normal budget balance.

# Ready to test
# Test success and I am now satisfied with the display

# Ready for grading
