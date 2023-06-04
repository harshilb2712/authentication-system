def signUp():
    print('Welcome to Skillslash SignUp Portal')
    while True:
        userUp = input('Enter a new username: ').lower()
        if userUp == '0':
            return 'Failed'
        
        elif userUp not in d:
            passUp = input('Enter a strong Password: ')
            checkPasswordStrength(passUp)
            confirmPassword(passUp)
            mobileNumber(userUp)
            d[userUp] = passUp    # d.update({userUp:passUp})
            return 'Successful'
        
        else:
            print('''Username already exists.
            Press 0 to Exit or
            Try again
            ''')
            
# signUp()

def mobileNumber(username):
    number = '123'
    if sendOTP(number):
        dmob[username] = number
        return True

def main():
    print('Welcome to Skillslash Web Portal')
    while True: 
        mode = input('''Press 1 for SignUp Page
        Press 2 for SignIn Page
        Press 0 to Close Website
        : ''')
        if mode == '1':
            print('SignUp', signUp())

        elif mode == '2':
            print('SignIn')
            signIn()
            
        elif mode == '0':
            print('Exiting')
            return 'Closed'

        else:
            print('Invalid input')

            
d = {'admin':'Qwerty@123'}
dmob = {'admin':'9354328855'}

main()