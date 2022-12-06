"""
Created By: Mikayla Ries
Created Date: 13 September 2022
Last Revised: 06 December 2022
Source used for math variables & computations:
https://youtu.be/6bLg_Ex0A-4
Added real estate info. from Jill Ries with RE/MAX Gulf Coast Living
Utilized "Karl's Mortgage Calculator App"
Additional coding resource - James Greene
"""


def exception_handler_float(prompt):
    """ Exception handler float function prompts user to provide a specific
    loan item (purchase_price, down payment, annual interest rate, annual HOA,
    annual property tax and annual home insurance). Function will re prompt
    user if they input 0, negative integer or characters.
    Then returns the resulting value."""
    good_input = False
    value = None
    while not good_input:
        try:
            value = float(input(prompt))
            if value > 0:
                good_input = True
            else:
                print("Please provide a positive value greater than 0.")
        except ValueError:
            print("Please exclude dollar sign, comma, and percentage symbol "
                  "characters.")
    return value


def exception_handler_hoa(annual_hoa_prompt):
    """ Exception handler HOA function prompts user to provide annual HOA fees.
     Function will re prompt user if they input a negative integer or
     characters. Then returns the resulting value."""
    good_input = False
    annual_HOA = None
    while not good_input:
        try:
            annual_HOA = float(input(annual_hoa_prompt))
            if annual_HOA >= 0:
                good_input = True
        except ValueError:
            print("Please exclude dollar sign, comma, and percentage symbol "
                  "characters.")
    return annual_HOA


def exception_handler_int(loan_term_prompt):
    """ Exception handler integer function prompts user to provide loan term
    in years. Function will re-prompt user if they input 0, negative integer
    or a decimal place. Then returns the resulting value. """
    good_input = False
    loan_term = None
    while not good_input:
        try:
            loan_term = int(input(loan_term_prompt))
            if loan_term > 0:
                good_input = True
            else:
                print("Please provide a positive value greater than 0. ")
        except ValueError:
            print("Please exclude decimal place and any additional "
                  "characters. ")
    return loan_term


def greet(name, msg):
    """ Greet function that takes name and message as parameters and user_name
     and "Let's get started with ..." as the arguments.
     """
    print("Hello", name + msg)


def main():
    """ The program calculates monthly mortgage payments including
    interest, monthly HOA costs, monthly property tax costs,
    and monthly homeowner's insurance costs.
    """
    # Prompts user to give their name and stores input in variable user_name.
    user_name = input("Hi, What is your first name? ")

    greet(user_name, ". Let's get started with calculating your "
                     "mortgage payments!")

    print("First I need to gather some information ... ")

    # end = "!" adds exclamation point to end of string.
    print(
        "Please note this program is currently only compatible with "
        "fixed-rate loans", end="!")

    # Prints blank line to space output for better user readability.
    print("\n")

    # Prompts user to give the property address and stores user input in
    # variable address.
    address = str(input("What is the address of the property? Please include "
                        "the full address. "))

    # Prints blank line to space output for better user readability.
    print("\n")

    # Prompts user to provide property purchase price. Functon call to
    # exception handler float. Stores resulting return value as purchase price.

    purchase_price_prompt = ("What is the property's purchase "
                             "price? (Please exclude dollar sign "
                             "and comma characters "
                             "(e.g., 200000.00)) ")
    purchase_price = exception_handler_float(purchase_price_prompt)
    # Prints blank line to space output for better user readability.
    print("\n")

    # Prompts user to provide down payment. Function call to exception
    # handler float. Stores resulting return value as down payment.
    down_payment_prompt = ("What is the down payment? (Please "
                           "place in decimal form and exclude percentage "
                           "symbol. (e.g., .20 )) ")
    down_payment = exception_handler_float(down_payment_prompt)
    # Prints blank line to space output for better user readability.
    print("\n")

    # Prompts user to provide annual interest rate. Function call to exception
    # handler float. Stores resulting return value as annual interest rate.
    annual_int_rate_prompt = ("What is the annual interest rate for your "
                              "mortgage? (Please place in decimal form and "
                              "exclude percentage symbol (e.g., .05)) ")
    annual_int_rate = exception_handler_float(annual_int_rate_prompt)
    # Prints blank line to space output for better user readability.
    print("\n")

    # Prompts user to provide annual HOA fees. Function call to exception
    # handler HOA. Stores resulting return value as annual HOA.
    annual_hoa_prompt = ("Please provide the annual HOA fees if applicable. "
                         "If you do not have any please type 0. "
                         "(Please exclude dollar sign and comma characters) ")

    annual_HOA = exception_handler_hoa(annual_hoa_prompt)

    # Prints blank line to space output for better user readability.
    print("\n")
    # Prompts user to provide loan term in years. Function call to exception
    # handler int. Stores resulting return value as loan term.
    loan_term_prompt = ("Please provide the fixed-rate loan term in years. "
                        "(Please exclude decimal place (e.g., 30)) ")
    loan_term = exception_handler_int(loan_term_prompt)

    # Prints blank line to space output for better user readability.
    print("\n")

    # Prompts user to provide annual property taxes. Function call to exception
    # handler float. Stores resulting return value as annual prop taxes.
    annual_prop_taxes_prompt = ("Please provide an annual property tax "
                                "estimate: (Please exclude dollar sign and "
                                "comma characters (e.g., 2140.00)) ")
    annual_prop_taxes = exception_handler_float(annual_prop_taxes_prompt)
    # Prints blank line to space output for better user readability.
    print("\n")

    # Prompts user to provide annual homeowner's insurance estimate. Function
    # call to exception handler float. Stores resulting return value as annual
    # home insurance.
    annual_home_insurance_prompt = ("Please provide an annual homeowner's "
                                    "insurance estimate. (Please exclude "
                                    "dollar sign and comma characters "
                                    "e.g., 3240.23)) ")
    annual_home_insurance = \
        exception_handler_float(annual_home_insurance_prompt)
    # Prints blank line to space output for better user readability.
    print("\n")

    # First part of calculations for principal loan amt by
    # multiplying down payment by purchase price.
    down_payment_sum = float(down_payment) * int(purchase_price)

    # Calculates loan amt by subtracting purchase price
    # from down_payment_sum.
    principal_loan_amt = int(purchase_price) - float(down_payment_sum)

    # Inclusion of modulus function %.  Calculates remainder of 7/2.
    remainder = 7 % 2
    print(remainder)

    # Calculates monthly interest rate.
    monthly_int_rate = annual_int_rate / 12

    # Calculate monthly HOA fees.  / division operator.
    monthly_HOA = annual_HOA / 12

    # Total number of months required to repay the loan.
    loan_months = loan_term * 12

    # Calculates monthly mortgage payment.
    # M=P (principal loan amt) x R (monthly interest rate).
    # * multiplication operator.
    complete_numerator = principal_loan_amt * monthly_int_rate
    # Denominator portion of M= 1 + R (monthly interest rate).
    # + addition operator.
    denom1 = 1 + monthly_int_rate
    # Denominator portion of M=1 + R (monthly interest rate) raised to the
    # negative n (loan term). ** exponentiation operator.
    denom2 = denom1 ** (-loan_months)
    # Denominator portion of M= 1 - (1 + R) raised to the negative n.
    # - subtraction operator.
    complete_denom = 1 - denom2
    # monthly_mortgage=numerator/denominator.
    monthly_mortgage = complete_numerator / complete_denom

    # Calculates exact monthly homeowner's insurance payment.
    monthly_home_ins = annual_home_insurance / 12

    # Calculates rough whole number estimate of monthly
    # homeowner's insurance.  // floor division operator.
    rough_home_ins = annual_home_insurance // 12
    print(rough_home_ins)

    # Calculates monthly property tax payment.
    monthly_prop_tax = annual_prop_taxes / 12

    # Calculates total monthly payment including prop. taxes,
    # monthly HOA fees, homeowner's insurance.  + concatenates
    # the strings together.
    total_monthly_payment = monthly_mortgage + monthly_home_ins \
        + monthly_prop_tax + monthly_HOA

    # Inclusion of shortcut operators. += operator adds annual_prop_taxes
    # plus annual_home_insurance and stores result
    # under variable name a.
    a = annual_prop_taxes
    a += annual_home_insurance

    # -= operator subtracts monthly_HOA from monthly_mortgage
    # and stores result under variable name b.
    b = monthly_mortgage
    b -= monthly_HOA

    # *= operator multiplies monthly_HOA by 12 and stores result under
    # variable name c.
    c = monthly_HOA
    c *= 12

    # /= operator divides annual_prop_taxes by 12 and stores result under
    # variable name d.
    d = annual_prop_taxes
    d /= 12

    # %= operator takes annual_prop_taxes divided by 3 and then stores the
    # remainder under the variable name e.
    e = annual_prop_taxes
    e %= 3

    # **= operator takes monthly_HOA and raises it to the 2nd power and stores
    # result in variable name f.
    f = monthly_HOA
    f **= 2

    # //= operator takes annual_home_insurance divided by 4 and stores the
    # nearest whole number result under variable name g.
    g = annual_home_insurance
    g //= 4

    # Prints summary of calculations to user.
    print(user_name + " " + "I have finished calculating your monthly "
                            "payments.")

    # Prints blank line to space output for better user readability.
    print("\n")

    # Counts down from 5 to 1.
    print("Drum roll please...")
    for x in range(5, 0, -1):
        print(x)

    # Prints blank line to space output for better user readability.
    print("\n")

    # Prints a total monthly payment message based on if the total monthly
    # payment is under $2500 a month, in between $2500 - $5000 a month, or over
    # $5000 a month.
    if total_monthly_payment < 2500:
        print("Good news! Your total monthly payment for" + " "
              + address +
              " " + "is less than $2500 a month.")
    elif (total_monthly_payment > 2500) and \
            (total_monthly_payment < 5000):
        print("Good news! Your total monthly payment for" + " "
              + address +
              " " + "is between $2500 to $5000 a month.")
    else:
        print("Your total monthly payment for" + " " + address +
              " " + "is over $5000 a month.")

    # Prints message about annual HOA costs if they do have a HOA fees or not.
    if 0 == annual_HOA:
        print("Congrats you also don't have a monthly HOA fee!")
    elif annual_HOA != 0:
        print("Don't forget about the HOA fees though!")

    # Prints blank line to space output for better user readability.
    print("\n")

    # Prints total monthly payment to user.
    format(total_monthly_payment, '.2f')
    print(
        "Your total monthly payment for" + " " + address + " " + "is"
        + " " + "$" +
        format(total_monthly_payment, '.2f'))

    print(
        "This includes your mortgage payment plus interest,"
        " homeowner's insurance, property taxes, and HOA costs.")

    # Prints blank line to space output for better user readability.
    print("\n")

    print("Here are the costs broken up:")

    # Print monthly HOA fee.  Sep. function adds the dollar sign before the
    # monthly HOA.
    print("Your monthly HOA cost is" + " ", format(monthly_HOA, '.2f'),
          sep='$')

    # Prints monthly property taxes.
    print("Your monthly property taxes are" + " " + "$" +
          format(monthly_prop_tax, '.2f'))

    # Prints monthly homeowner's insurance.
    print("Your monthly homeowner's insurance is" + " " + "$" + format(
        monthly_home_ins, '.2f'))

    # Prints blank line to space output for better user readability.
    print("\n")

    # Coupon code offered for future mortgage calculator if it was your first
    # time using it. Try except block ensures user inputs correct values.
    good_feedback = False
    while not good_feedback:
        try:
            new_customer = int(input('Thanks for using our services. '
                                     'Was this your first time with us? '
                                     'Please type 1 for yes and 0 for no.'))
            if new_customer == 1:
                print("\n")
                print("Thanks for thinking of us! Here is a discount code "
                      "for 20% "
                      "off your next visit. Coupon code: 13GZ57F.")
                good_feedback = True
            elif new_customer == 0:
                print("Thanks for being a loyal customer!")
                good_feedback = True
        except ValueError:
            print("Please type 1 for yes and 0 for no.")
    # Prints blank line to space output for better user readability.
    print("\n")

    # Asks user to provide rating on interface. Try except block
    # ensures user inputs correct values.
    good_interface = False
    interface_rating = None
    while not good_interface:
        try:
            interface_rating = int(input("Take a quick second to rate our"
                                         " program. How satisfied were you on "
                                         "a scale of 1 to 5 with the "
                                         "interface?"))
            if interface_rating > 5 or interface_rating < 1:
                print("Please rate how satisfied you were on a scale of 1 to 5"
                      " with the interface.")
            else:
                good_interface = True
        except ValueError:
            print("Please rate how satisfied you were on a scale of 1 to 5.")
    # Asks user to provide rating on the layout. Try except block ensures user
    # inputs correct values.
    good_layout = False
    layout_rating = None
    while not good_layout:
        try:
            layout_rating = int(input("How satisfied were you on a scale of 1 "
                                      "to 5 with the layout?"))
            if layout_rating > 5 or layout_rating < 1:
                print("Please rate how satisfied you were on a scale of 1 "
                      "(not very satisfied) to 5 (very satisfied)"
                      " with the layout.")
            else:
                good_layout = True
        except ValueError:
            print("Please rate how satisfied you were on a scale of 1"
                  " (not very satisfied) to 5 (very satisfied).")
    # Prints message based on both ratings.
    if interface_rating >= 4 or layout_rating >= 4:
        print("\n")
        print("Thanks for the kind rating!")
    elif interface_rating <= 4 and layout_rating <= 4:
        print("\n")
        print("Thanks for your input. We've noted your feedback.")

    # Prints end statement to user. * prints string 5 times.
    print("\n")
    print("Bye Now!" * 5)


if __name__ == "__main__":
    main()
