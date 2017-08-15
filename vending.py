sodas = ['Pepsi', 'Coke Zero', 'Sprite']
chips = ['Doritos', 'Fritos']
candy = ['Snickers', 'M&Ms', 'Twizzlers']

while True:
    choice = input("Would you like a SODA, some CHIPS, or a CANDY? > ").lower()

    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack = candy.pop()
        elif choice == 'quit' or choice == 'exit':
            break
        else:
            print("Sorry, I didn't understand that. Please make another choce.")
            continue
    except IndexError:
        print("Sorry, there are no more {} items available.".format(choice))
        continue
    else:
        print("Here is your {choice}: {snack}".format(choice=choice, snack=snack))
