####################################
#        Author: Amber Lee         #
# Email: cryptoboxcomics@gmail.com #
#      Info: A choose-your-own     #
#          adventure game          #
####################################

player_name = ""
player_level = 1
player_species = "Human"

####################################
#            Game Start!           #
####################################

###         Introduction         ###

print()
print()
print("   ####################################################")
print("   # Hello! This is a choose-your-own-adventure race. #")
print("   #  Make right decision with turns on the race track#")
print("   #       and be first at the finishline!            #")
print("   #             BEST OF LUCK SPEEEDY                 #")
print("   ####################################################")
print()
print()

while(player_name == ""):
    player_name = input("What is your name, Racer? : ")

print()
print("Welcome, " + player_name + "! You are about to start adventurous race with World Top Racers ")
print("You start off with slowest race car Honda Civic)) and depending on your decisions the vehicle model and speed will upgrade or downgrade")
print()

#    ---Section Author: <Akhror>---   #
print("The race started and you are the last, make following choices ... ")
print("1. Hit the speed all they way to the floor")
print("2. Let the car to warm up a bit before speeding")
decision = input("Pick your choice: ")
print()
if (decision == "1"):
    print("You car is overheated, you`re out of race")
    player_level = player_level - 0
elif (decision == "2"):
    print("Good work, the car is upgraded to Subaru race car")
    player_level = player_level - 10
print("Your driving skills are average now, suddenly your coach called you to pit stop ...")
print("1. Went to pit stop as soon as possible")
print("2. Ignore the message and keep going ")
decision = input("What would you do?: ")
print()
if (decision == "1"):
    print("Nice, you got new BMW ")
    player_level = player_level - 50
elif (decision == "2"):
    print("Quickly ran out of the fuel and stopped at middle of the race ")
    player_level = player_level - 5
print("The flag went up for last circle and your alarm started ringing zzz zzz ...")
print("1. Let the alarm go to snooze and keep racing")
print("2. Woke up and get ready to work")
decision = input("What is your action?: ")
print()
if (decision == "1"):
    print("Congrats, you are late for work again")
    player_level = player_level - 33
elif (decision == "2"):
    print("Congrats, you made another 5$ towars your real race car")
    player_level = player_level - 99
#            ---section end---           #

