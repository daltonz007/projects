print("Welcome To The Game")
name = input("What is your name? ")
age = int(input("What is your age? "))
print("Hello", name, "you are", age, "years old. ")
health = 10
is_older = age >= 13
if age >= 13:
  print("You are old enough. ")
  print("You have", health, "health. ")
  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    print("Let the game begin. ")
    left_or_right = input("Do you want to go left or right? (left/right) ")
    if left_or_right == "right":
      print("YOU DIED")
    else:
      ans = input("You approach a lake. Do you swim across or go around? (across/around) ")
      if ans == "across":
        print("You swam acrossed, but were attacked by a lake monser and lost 5 health. ")
        health -= 5
      elif ans == "around":
        print("You made it around the lake. ")
      ans = input("You notice a house and a barn. Which do you go to? (house/barn) ")
      if ans == "house":
        print("You have reached safety. YOU WIN! ")
      else:
        print("You were trampled by a horse. YOU DIED. ")
elif age >= 9: 
  print("You may play with parental supervision. ")
  print("You have", health, "health. ")
  wants_to_play = input("Do you want to play? ").lower()
  if wants_to_play == "yes":
    print("Let the game begin. ")
    left_or_right = input("Do you want to go left or right? (left/right) ")
    if left_or_right == "right":
      print("YOU DIED")
    else:
      ans = input("You approach a lake. Do you swim across or go around? (across/around) ")
      if ans == "across":
        print("You swam acrossed, but were attacked by a lake monser and lost 5 health. ")
        health -= 5
      elif ans == "around":
        print("You made it around the lake. ")
      ans = input("You notice a house and a barn. Which do you go to? (house/barn) ")
      if ans == "house":
        print("You have reached safety. YOU WIN! ")
      else:
        print("You were trampled by a horse. YOU DIED. ")
else:
  print("You must be at least 13 years old to play this game. ")
