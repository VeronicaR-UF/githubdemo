def Menu():
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')
    return None

def decode(password):
    for ii in range(0, len(password), 1):
        if password[ii] == '7':
            password2 += '0'
        elif password[ii] == '8':
            password2 += '1'
        elif password[ii] == '9':
            password2 += '2'
        else:
            password2 += str(int(password[ii]) + 3)
    return password2


action = 0
password = '00000000'
password2 = ''

Menu()
while action != 3:
    action = int(input('Please enter an option: '))
    if action == 1:
        password = (input('Please enter your password to encode: '))
        print('Your password has been encoded and stored!')
    elif action == 2:
        password2 = decode(password)
        print(f'The encoded password is {password2}, and the original password is {password}')
    elif action == 3:
        action = 3
    else:
        print('Not a valid option.')
