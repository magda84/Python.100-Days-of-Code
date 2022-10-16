print('''
 
  .-"""-.
 / _   _ \
 ](_' `_)[
 `-. N ,-' 
   |   |
   `---'

''')

print("***Welcome to the Skull Island!***\nWill you survive?")

intro = input("You suddenly awake and find yourself in an unknown area. Two paths are in front of you.\n"
              "One with a rope ladder that descends to the sea and a dark cave in front of you. "
              "Which path do you choose?\n"
              "Press [a] for the path to the sea or [b] for the cave: \n").lower()
if intro == "a":
    print("Oh, no! The ropes and broken and...guess what?\nYOU ARE DEAD.")
    exit()
elif intro == "b":
    print("You enter the cave. Some matches and a bottle of whiskey is left there by it's former inhabitant.\n"
          "You pick up the items.")
else:
    print("You stay scared and trapped on the same spot until you starve to death.\nGAME OVER.")
    exit()
print('''
       _________
       \        \
        \  -dd-  \
         \        \
          \        \
           )--------)
          //)/)/)  /
         ///////  /
        ///////  /
       ///////  /
      /""""""""/
     /____<()_/
           ||
           ||
           ||
           ||
           ||

''')

print("------------->>>\nINVENTORY ITEMS: +1 MATCHES | +1 WHISKEY")


print("You still feel dizzy and up to this time, you can not understand how you got here.\n"
      "Weird ideas, like obsessions are crossing your mind. And yet, you are unsure what to do....")
print("YOU SAY:")
cave = input("-I really need to light up a match and take a closer look to the area. (Press [a]):\n"
             "-W....wait! What's that smell? Flammable whiskey?"
             " Maybe I have to take a second thought on this. (Press [b]): \n"
             "-S-s-s-s-sooo cold! But these items will be really handy."
             "I just need to exit the cave and light a fire.\n"
             "Choose: [a], [b] or [c]:\n").lower()

if cave == "a":
    secret_of_life = input("Hey, you're brave! You light up the match and what do you see?\n"
                           "Well, it's an envelope that reads: S.O.L! That stands for the Secret Of Life!\n"
                           "Are you excited? Press [a] to read this!")
    if secret_of_life == "a":
        print("With shaken hands you open the envelope....It reads:\n"
              "If you played this game\n"
              "Y O U  H A V E  N O  L I F E...")
    else:
        print("You lose just a sec before the greatest revelation of your life...C'mon!")
        exit()

elif cave != "a":
    cave_2nd_choice = input("Hmmm, that wasn't the brightest idea! I'll give you though a second chance.\n"
                            "Press [a], [b] or [c]: ")
    if cave_2nd_choice == "a":
        secret_of_life = input("You found it! It's an envelope that reads: S.O.L! That stands for the Secret Of Life!\n"
                               "Are you excited? Press [a] to read this!: ")
        if secret_of_life != "a":
            print("You lose just a sec before the greatest revelation of your life...C'mon!")
            exit()

        else:
            print("With shaken hands you open the envelope. It reads:\n"
                  "*************************\n"
                  "Congratulations! If you played this game\n"
                  "Y O U  H A V E  N O  L I F E...")
    else:
        print("You lose just a sec before the greatest revelation of your life...C'mon!")
        exit()
else:
    print("You lose just a sec before the greatest revelation of your life...C'mon!")
    exit()
