from random import randint
class Numberguess:
    
    randomNum = -1
    def __init__(self,rangefrom,rangeto):
        self.rangefrom = rangefrom
        self.rangeto = rangeto
    
    def generateRandom(self):
        self.randomNum = randint(self.rangefrom,self.rangeto)
    
    def __str__(self):
        return f"system selected random Number was {self.randomNum}"
        
    def guessNumber(self, guess):
        if guess < self.randomNum:
            print("genrated number is greater than your number")
            return False
        elif guess > self.randomNum:
            print("genrated number is lesser than your number")
            return False
        else:
            print("You Found the number.")
            return True

if __name__ == '__main__':
    ...