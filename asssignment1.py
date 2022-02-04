print("                                                                                           \033[1;33mRajwinder Kaur 5295037")
#\033[1;33m is color code for text in 'Yellow'
def cal():
    number_1 = int(input('\033[1;38mPlease enter the first number: ')) #\033[1;30m is color code for text in 'White'
    number_2 = int(input('Please enter the second number: '))
    x = input('press * for multiplication : ')
    if x == '*':
        print('\033[1;34m{} * {} = '.format(number_1, number_2), number_1 * number_2) #\033[1;30m is color code for text in 'Cyan'

    else:
        print('\033[1;31mYou have not typed a valid operator, please run the program again.') #\033[1;31m is color code for text in 'Red'

cal()