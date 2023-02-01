import random
l=["rock","paper","scissor"]

while True:
    uc=int(input('''
    Game start
    1. Yes
    2. No        
    '''))

    scoreu=0
    scorec=0

    if uc==1:
          for a in range(1,5):
              userinput=int(input('''
              1.rock
              2.paper
              3.scissor
              
                 '''))
              if userinput ==1:
                  uchoice="rock"
              elif userinput==2:
                  uchoice = "paper"
              elif userinput ==3:
                  uchoice="scissor"
              comp=random.choice(l)

              print("User input : ",uchoice)
              print("User input : ",comp)

              if uchoice=="rock" and comp=="scissor":
                   print("user win")
                   scoreu=scoreu+1
              elif uchoice == "paper" and comp == "rock":
                   print("user win")
                   scoreu = scoreu + 1
              elif uchoice == "scissor" and comp == "paper":
                   print("user win")
                   scoreu = scoreu + 1
              elif uchoice==comp:
                   print("game draw")
              else:
                  print("computer won")
                  scorec = scorec + 1

          print("******User score***** : ",scoreu)
          print("******Computer score***** : ", scorec)

          if scoreu>scorec:
              print("User won")
          elif scorec>scoreu:
              print("Computer won")
          else:
              print("Game draw")

    else:
        break