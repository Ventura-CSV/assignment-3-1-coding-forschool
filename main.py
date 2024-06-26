import random


def main():
    number1 = random.randint(0, 100)
    number2 = random.randint(0, 100)
    number3 = random.randint(0, 100)

    min_value = 0
    
    if number1 < number2 and number1 < number3:
        min_value = number1
    elif number2 < number1 and number2 < number3:
        min_value = number2
    else:
        min_value = number3    

    print(f'{min_value}')
    ########################################
    # Do not delete the return statement
    ########################################
    return number1, number2, number3, min_value


if __name__ == '__main__':
    main()
