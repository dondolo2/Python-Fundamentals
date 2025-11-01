# Exercise 2: Functions with and without Parameters
# We will also put into practice what you did or learned on control structures
# Please mind your arguments!!!!


# 1. Write a function without a parameter called 'get_user_input'
    # This function must take user inputs 'Username, age and email'
    # validate the AGE using a loop and conditional statements
        # If the AGE is not an Integer print "Not an Integer, Enter a valid age!"
        # If the AGE is less than 17 print "You are young"
        # If the Age is more than 65 print "You are too old"  
    # Return all the inputs
def get_user_input():
    username = input("Enter your Username: ")

    while True:
        age_input = input("Enter your Age: ")
        if not age_input.isdigit():  
            print("Not an Integer, Enter a valid age!")
            continue  

        age = int(age_input)

        if age < 17:
            print("You are young")
        elif age > 65:
            print("You are too old")
        else:
            break

    email = input("Enter your email address: ")
    return username, age, email




# 2. On the function below 'validate_username'
    # Validate the username that comes as a parameter
    # Use a loop to check all the characters on the username 
    # If the chars are not strings return False else return True
    # If the username is an empty string return False
    # Return the boolean

def validate_Username(username) -> bool:
    if username == "":
        return False
    for char in username:
        if not char.isalpha():
            return False
        else:
            pass
       
    return True


# 3. Pass the parameters to the function below 'display_user_info'
    # Underneath the User Information print the following:
        # 'Username : <username>'
        # 'Age      : <age>'
        # 'Email    : <email>
    # return 'Thanks!, Details captured.'

def display_user_info(username, age, email):
    print(f"Username : {username}")
    print(f"Age      : {age}")
    print(f"Email    : {email}")
    return "Thanks!, Details captured."
   

# 4. Call all the functions
    # If 'validate_username' function returns False
        # write a loop to and take new input for the username and take it to be evaluated 'validate_username'
    # if 'validate_username' returns True then you can display the user Info   
def main():
    username, age, email = get_user_input()

    while not validate_Username(username):
        print("Invalid username! Please try again.")
        username = input("Enter a valid Username: ")

    print(display_user_info(username, age, email))


if __name__ == "__main__":
   #call the main function
    main()