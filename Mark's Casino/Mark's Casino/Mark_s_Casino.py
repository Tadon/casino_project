balance = int(input("Initial deposit amount: $"))
import random
import time

#  Defined Functions  # 
def open_print_menu():
    #This is the menu the user selects from to make their choice.
    print("Welcome to Mark's casino! Please select from the following:")
    print("1: Play Slots")
    print("2: Play Craps")
    print("3: Play Blackjack")
    print("4: Deposit more funds")
    print("5: Withdraw funds")
    print("6: Exit")
    menuSelection = int(input("Make your selection here: "))
    return menuSelection
def play_game_slots(balance):
#This is a function that takes the balance as a parameter, allows you to play slots, then returns the final value of balance
    while True:        
        if balance <= 0:
            print("Insufficient funds! Please deposit more funds.")
            break
        wagerAmt = int(input("Welcome to Mark's Super Lucky Slot Machine! Enter your wager amount here: $"))
        while True:                 
            while wagerAmt > balance:
                wagerAmt = int(input("You can't bet more than your balance! Enter valid wager here: $"))
            reel1 = random.randint(1,7)
            reel2 = random.randint(1,7)
            reel3 = random.randint(1,7)
            print("#######################################")
            print(reel1, end = "", flush = True)
            time.sleep(0.5)
            print(reel2, end = "", flush = True)
            time.sleep(0.5)
            print(reel3)
            print("#######################################")
            if(reel1 == reel2) and (reel2 == reel3):
                print("WINNER! You've just won 100x your wager!")
                balance = balance + wagerAmt * 100
                print(f"Your new balance is ${balance}")
                playAgain = str(input("Enter 1 to play again, 2 to change your Wager or any other button to return to the main menu: "))
            elif (reel1 == reel2) or (reel2 == reel3) or (reel1 == reel3):
                print("WINNER! You've just won 10x your wager!")
                balance = balance + wagerAmt * 10
                print(f"Your new balance is ${balance}")
                playAgain = str(input("Enter 1 to play again, 2 to change your Wager or any other button to return to the main menu: "))
            else:
                balance = balance - wagerAmt
                print("Sorry, better luck next time!")
                print(f"Your new balance is ${balance}")
                if balance == 0:
                    print("Your balance has reached $0. Please deposit more funds to continue")
                    break
                playAgain = str(input("Enter 1 to play again, 2 to change your Wager or any other button to return to the main menu: "))
            if playAgain == '2':
                wagerAmt = int(input("Enter new Wager amount: $"))
            if playAgain != '1' and playAgain != '2':
                break
        
        break
    return balance
def perform_deposit_funds(balance):
    #This function allows the user to add funds to their current balance, and returns user after deposit amount is finalized
    while True:
            deposit = int(input(f"Current balance is ${balance}. Enter deposit amount to be added to your balance: $"))
            balance = balance + deposit
            print(f"Thank you! Your new balance is ${balance}")
            break
                
    return balance
def perform_withdraw_funds(balance):
    #allows the user to withdraw funds from their current balance, throws error if user tries to 
    #withdraw more money than they currently have in their balance
    while True:
        if balance <= 0:
            print("You have no balance! How can you possibly withdraw?")
            break
        while True:                
            withdraw = int(input(f"Current balance is ${balance}. Enter amount to withdraw: $"))
            while withdraw > balance:
                withdraw = int(input("You can't withdraw more than your balance! Enter valid amount: $"))
            balance = balance - withdraw
            print(f"Thank you! Your new balance is ${balance}")
            break            
        break
    return balance
#craps functions
def play_game_craps(balance):
    while True:   
        exit_game = False
        if balance <= 0:
            print("Insufficient funds! Please deposit more funds.")
            break
        print("Welcome to Mark Always Wins craps! Please select from the following menu!")
        print("1: Play craps!")
        print("2: Deposit funds.")
        uSelection = int(input("3: Exit."))
        if uSelection == 2:
            balance = perform_deposit_funds(balance)
        if uSelection == 3:
            return balance
        if uSelection == 1:
            while True and not exit_game:
                wagerAmt = int(input("Welcome! Please enter your Wager amount here: "))
                while wagerAmt > balance:
                    wagerAmt = int(input("You can't bet more than your balance! Enter valid wager here: $"))
                
                while True and not exit_game: 
                    play_craps = str(input("Enter 1 to exit or any button to roll!."))
                    if play_craps != '1':
                        dice1 = random.randint(1,6)
                        dice2 = random.randint(1,6)
                        print("#######################################################")
                        print(f"Your come out roll was {dice1} and {dice2}")
                        print("#######################################################")
                        if (dice1 + dice2 == 7) or (dice1 + dice2 == 11):
                            print(f"Nice come out roll! You win ${wagerAmt}!")
                            balance = balance + wagerAmt
                            print(f"Your new balance is ${balance}")
                        elif (dice1 + dice2 == 2) or (dice1 + dice2 == 3) or (dice1 + dice2 == 12):
                            print("Ouch! You lose on the come out roll")
                            balance = balance - wagerAmt
                            print(f"Your new balance is {balance}")
                        else:
                            while True:
                                sRoll = str(input("Enter any button here for your next roll!"))
                                dice3 = random.randint(1,6)
                                dice4 = random.randint(1,6)
                                print("#######################################################")
                                print(f"You rolled a {dice3} and a {dice4}!")
                                print("#######################################################")
                                if (dice3 +dice4) == (dice1 + dice2):
                                    winnings, balance = pay_game_craps(balance,wagerAmt,dice1,dice2)
                                    print(f"You win! Your winnings are {round(winnings, 2)}. Your new balance is {round(balance, 2)}")
                                elif (dice3 + dice4) == 7:
                                    balance = balance - wagerAmt
                                    break
                                    print(f"Sorry! You lose {round(winnings, 2)}. Your new balance is {round(balance, 2)}")
                                else:
                                    continue
                                    
                    if play_craps == '1':
                        exit_game = True
                    
        break
    return balance
def pay_game_craps(balance, wagerAmt,dice1, dice2):
    global winnings
    if dice1 + dice2 == 4:
        winnings = wagerAmt * 1.8
    elif dice1 + dice2 == 5:
        winnings = wagerAmt * 1.4
    elif dice1 + dice2 == 6:
        winnings = wagerAmt * 1.2
    elif dice1 + dice2 == 8:
        winnings = wagerAmt * 1.2
    elif dice1 + dice2 == 9:
        winnings = wagerAmt * 1.4
    elif dice1 + dice2 == 10:
        winnings = wagerAmt * 1.8
    else:
        print("Error!")
    balance = round(balance, 2) + round(winnings, 2)
    return winnings, balance
#Blackjack
def play_game_blackjack(balance):
    while True: 
        exit_game = False
        if balance <= 0:
            print("Insufficient funds! Please deposit more funds.")
            break
        print("Welcome to Mark's Blackjack! Blackjack pays 3 to 2. Please select from the following menu")
        print("1: Play Blackjack!")
        print("2: Deposit funds.")
        uSelection = int(input("3: Exit."))
        if uSelection == 2:
            balance = perform_deposit_funds(balance)
        elif uSelection == 3:
            return balance
        elif uSelection == 1 and not exit_game:
            wagerAmt = int(input("Welcome to Blackjack! How much would you like to wager?"))
            while wagerAmt == 0 or wagerAmt < balance:
                uuSelection = str(input("Incorrect value. Please wager greater than 0 and no more than your total balance. Press 1 to exit or any other button to return to the previous menu"))
                if uuSelection == '1':
                    return balance
                else:
                    break
            
def card_generator():
    values = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suits = ['♠', '♡', '♢', '♣']
    value = random.choice(values)
    suit = random.choice(suits)
    card = (value, suit)
    return card


#Makes sure your initial balance is greater than zero before it allows you to open the casino.
while balance <= 0:
    balance = int(input("Your balance is at zero! Enter amount to deposit here: $"))

#Main function
while True:
#initial menu
    menuSelection = open_print_menu()

#Selection 1 - Slots!
    if menuSelection == 1:
        balance = play_game_slots(balance)
        continue
#Selection 2 - Craps
    elif menuSelection == 2:
        balance = play_game_craps(balance)
        continue
#Selection 3 - Blackjack
    elif menuSelection == 3:
        balance = play_game_blackjack(balance)
        continue    
#Selection 4 -  depositing more funds
    elif menuSelection == 4:
        balance = perform_deposit_funds(balance)
        continue
 
#Selection 5 - withdrawing funds
    elif menuSelection == 5:
        balance = perform_withdraw_funds(balance)
        continue
    
#Selection 6 - Exiting program
    else:
        break

#Exit program message
print(f"Thank you for playing! Your remaining balance is ${balance}.")

