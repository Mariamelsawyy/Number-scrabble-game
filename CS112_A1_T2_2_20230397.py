# File:CS112_A1_T2_2_20230397.py.
# purpose: is to get three numbers from two players and if any one of them get 15 first ,then he is the winner
# Author: Mariam Mohamed Ahmed Elsawy
# ID: 20230397
list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] #list which the players must choose a number from it
sum1 = 0 # sum of player1
sum2 = 0 # sum of player2
count1 = 0 # to know  how many number of times that the first player play
count2 = 0 # to know how many number of times that the second player play
i = 0
for i in range(len(list_numbers) + 1):
    while sum1 <= 15 or sum2 <= 15:
        if sum1 > 15 or sum2 > 15:
            print("game is draw")
        player1 = int(input("Player1:please enter your number ")) #get the number from player1
        count1 += 1
        while True :
            if player1 in list_numbers:  # to check if the number that the player1 choose is in list_number or not
                list_numbers.remove(player1) # to prevent the repeating  of any number
                print(list_numbers)
                break
            else:
                player1 = int(input("please enter a valid number")) #to choose the number from list_number
        sum1 += player1
        print(sum1)
        if sum1 == 15 and count1 == 3:
            print("player1 is the winner")
            break
        elif sum1 == 15 and count1 > 3:
            print("game over")
            break
        player2 = int(input("Player2: please enter your number ")) #get the number from  player2
        count2 += 1
        while True:
            if player2 in list_numbers:# to check if the number that the player2 choose is in list_number or not
               list_numbers.remove(player2)  # to prevent the repeating  of any number
               print(list_numbers)
               break
            else:
                player2 = int(input("please enter a valid number")) #to choose the number from list_number
        sum2 += player2
        print(sum2)
        if sum2 == 15 and count2 == 3:
            print("player2 is the winner")
            break
        elif sum2 == 15 and count2 > 3:
            print("game over")
            break
    break