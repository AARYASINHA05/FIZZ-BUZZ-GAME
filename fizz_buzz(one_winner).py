# -*- coding: utf-8 -*-
"""fizz_buzz(one winner).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rupGJ7VYl77n-sa2FvFEDfKyVdvzMC_f
"""

# fizz buzz
while True:
  print("READY TO PLAY - 'FIZZ BUZZ'")

  ask=input("Type 'y' for YES or 'n' for NO - ")
  #if yes - this block is executed ----
  if ask=='y' or ask=='Y':
    print("HOW TO PLAY : ")
    print()
    print("Now, Players take turns to count incrementally, replacing any number divisible by three with the word 'FIZZ', and any number divisible by five with the word 'BUZZ', and any number divisible by both three and five with the word 'FIZZBUZZ'.")
    print()
    no_of_players=int(input("enter the number of players playing the game : ")) #asking for the number of players playing the game.
    print()

    lnames=[]
    for i in range(no_of_players):
      print("Enter the name of player",i+1,": ") #asking for the names of the players.
      a=input()
      lnames.append(a)
      print()

    """
    #in this block,
    #the names of the player is displayed when its their turn to enter their input[be it number or fizz or buzz or fizzbuzz]
    #then the player's input is checked and when wrong answer is entered by the player - that particular player gets removed from the game
    #then the game starts from the beginning with remaining players and the game continues until we get the winner
    """
    count=0
    while True:
      turn=lnames[0]
      if count>0:
        print("Restarting the game from the beginning ... ")
      print()


      n=0
      c=0
      i=1
      while True:
        print("It is your turn, ",turn)
        ans=input("enter the number :")
        #checking if the input is fine or not
        if (ans!=str(i) and (i%3!=0 or i%5!=0 or (i%3!=0 and i%5!=0))) and ans!="fizz" and ans!="buzz" and ans!="fizzbuzz":
          print("Please, enter the correct number...")
          print("enter the number, again, "+ turn +" : ", end=" ")
          ans=input()

        if i%3==0 and i%5==0:
          if ans.lower()!="fizzbuzz":
            lnames.remove(turn)
            no_of_players-=1
            print(turn," is out of the game :') ")
            print()
            break
        else:
          if i%3==0:
            if ans.lower()!="fizz":
              lnames.remove(turn)
              no_of_players-=1
              print(turn," is out of the game :') ")
              print()
              break
          elif i%5==0:
            if ans.lower()!="buzz":
              lnames.remove(turn)
              no_of_players-=1
              print(turn," is out of the game :') ")
              print()
              break
          else:
            pass
        if n<no_of_players-1:
          n+=1
        else:
          n=0
        turn=lnames[n]
        i+=1

      if len(lnames)==1:
        break
      count+=1

    print()
    print("The Winner is ")
    for i in lnames:
      print(i)
    print()
    print()

  elif ask=='n' or ask=='N':
    break

  else:# if the user enters a character other than (y,n,Y,N)
    print()
    print("please enter 'y' or 'n'")
    print()
    continue
