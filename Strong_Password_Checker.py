

import re
import getpass

'''Conditions:-

at least 1 uppercase
at least 1 lowercase
at least 1 digit
at least 1 special character
Minimum 8 characters'''

while True:

    
    errors=[]

    password=getpass.getpass('Hello Buddy, Please Enter Your password:')

    pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%!*?&])[a-zA-Z\d@#$!%*?&]{8,}$'

    
    if len(password)<8:
       errors.append('Password must be at least 8 characters')
    elif not re.search('[a-z]',password):
       errors.append('Please add at least one lowercase letter')
    elif not re.search('[A-Z]',password):
       errors.append('Please add at least one uppercase letter')
    elif not re.search(r'\d',password):
      errors.append('Please add at least one digit')
    elif not re.search(r'[@#$%&*!?]',password):
       errors.append('Please add at least one special character')

    if errors:
        print('\nWeak password:')
        for error in errors:
          print(' - ',error)
        print('\nTry again...\n')

    else:
       print(' Strong Password:✅')
       break
    