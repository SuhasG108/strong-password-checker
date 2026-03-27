

import re

'''Conditions:

1 uppercase
1 lowercase
1 digit
1 special character
Minimum 8 characters'''

password=input('Enter password:')

pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%!*?&])[a-zA-Z\d@#$!%*?&]{8,}$'

    
if len(password)<8:
    print('Password must be at least 8 characters')
elif not re.search('[a-z]',password):
    print('Add a lowercase letter')
elif not re.search('[A-Z]',password):
    print('Add an uppercase letter')
elif not re.search(r'\d',password):
    print('Add a number')
elif not re.search(r'[@#$%&*!?]',password):
    print('Add a special character')
else:
    print('Strong Password:✅')