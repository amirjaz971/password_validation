def pass_validation(password): 
    special_chars=('!','@','#','$','%','&','*') 
    not_valid=True

    while not_valid:
        num_count=0
        special_char_count=0
        
           
        if ' ' in password:
            print("You can't use space character to define your password!")
            password=input('Please enter another password again: ')
        elif len(password)<7:
            print('Your password must be at least 7 characters!')
            password=input('Please enter another password again: ')
        else:
            for i in password:
                if i in special_chars:
                    special_char_count+=1
                if i.isnumeric():  #The method for recognizing numbers in string
                    num_count+=1
            if num_count>=2 and special_char_count>=2:
                print('Strong')
                print('The password is valid')
                not_valid=False
            else:
                print('Weak')
                print('Try stronger password!')
                password=input('Please enter another password again: ')

password=input('Please enter the password: ')

pass_validation(password)


                        



