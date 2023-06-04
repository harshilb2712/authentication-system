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
            
main()
