date = input("Enter today's date: ")
mood_level = input("Enter mood level (1 to 10): ") + "\n"
thoughts = input("Let all your thoughts go:\n ")

##########to do's ################
# check if date exist, if  true append notes
# write to postgressql lite instead of text file
# write docs!
# prevent/ reformat t=dat entry




with open(f"data/{date}.txt", 'w') as file:
    file.write(mood_level)
    file.write(thoughts)


