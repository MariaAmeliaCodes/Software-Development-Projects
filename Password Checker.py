
while True:
    try:
        password = input("Enter a password: ")
        lower = False
        upper = False
        digit = False
        specialcharacter = False
        characters = 0

        special_character = "!#@&$¡¿?*+%/().=<>-_[]" 

        for item in password:

            characters += 1

            if item.islower():
                lower = True

            elif item.isupper():
                upper = True

            elif item.isdigit():  
                digit = True
            
            elif item in special_character:
                specialcharacter = True

        if lower == False:
            raise ValueError("Password must include at least one lowercase letter.")

        if upper == False:
            raise ValueError("Password must include at least one uppercase letter.")
        
        if digit == False:
            raise ValueError("Password must include at least one number.")
        
        if specialcharacter == False:
            raise ValueError("Password must include at least one special character.")
        
        if characters < 10:
            raise ValueError("Password must have at least 10 characters.")

        print("Password valid.")
        break

    except ValueError as e:
        print(e)

    
