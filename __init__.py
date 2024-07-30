from Numberguess import Numberguess

def main():
    print("Let's play Number guessing game today.")
    print("please enter the number range you want to play and you will have 5 chances to play")
    rangefrom = int(input("from: "))
    rangeto = int(input("to: "))
    
    numberguess = Numberguess(rangefrom, rangeto)
    numberguess.generateRandom()
    
    MAX_TRY = 5
    tries = 0
    found = False
    
    while tries < MAX_TRY:
        guess = int(input("type your guess: "))
        tries += 1
        if numberguess.guessNumber(guess):
            found = True
            break
        
    if(found is False):
        print('Better luck next time!')
    print(numberguess)
    
if __name__ == "__main__":
    main()