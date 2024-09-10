import random 

class Player:
  player = ""
  playerscore = 0

  def gamestart(self):
    self.number = random.randint(0,7)
    self.guesss = 0
    self.list = []
    self.limit = 3
    print()
    print("Guess what number I'm thinking off")
    print()
    print("Might even give you a hit if you do well enough")
    print()

    while self.limit > 0:
      self.player_guess = int(input("Well? What are you waiting for? Start guessing:"))
      print()

      if self.player_guess > 7 or self.player_guess < 0:
        print("Wow that was a terrible guess, think harder or we might be here all week long")
        print("also,", self.player_guess , "is not in the range...")
        print("Becareful though, you only have", self.limit, "guesss left")
        
      elif self.player_guess > self.number:
        self.guesss += 1
        self.limit-= 1
        print("WRONG")
        print(self.player, "You only have", self.limit, "guesss left")
        self.list.append(self.player_guess)
        
      elif self.player_guess < self.number:
        self.guesss += 1
        self.limit -= 1 
        print("oh oh... wrong again!")
        print()
        print(self.player, "You only have", self.limit, "guesss left.")
        self.list.append(self.player_guess)
        
      else:
        self.limit -= 1
        self.playerscore += 1
        self.list.append(self.player_guess)
        print()
        print("wow, you actually got it right")
        print()
        print(self.player_guess, "IS THE CORRECT ANSWER!")
        print()
        print("you only had",self.limit,"left too...")
        print("Lets see all the numbers you guessed")
        print()
        
        for i in self.list:
          print(i)
        self.list.clear()