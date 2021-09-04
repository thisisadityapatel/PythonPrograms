import csv
#getting the dtat from all the responses which we got from the making a google Form wich asked two main questions:
#1 what is the sport that the user watches the most
#2 what sports do they play the most
#these responses will be then rcorded and then finally stored in a dictionary where we will be counting the total number of sport every user watched and plays

watch = {}
play = {}

with open("sport.csv", "r") as file:
    read = csv.DictReader(file)

    for row in read:
        watch_name = row["Watch"]
        play_name = row["Play"]

        if watch_name not in watch:
            watch[watch_name] = 0
        watch[watch_name] += 1

        if play_name not in play:
            play[play_name] = 0
        play[play_name] += 1

print()
print("Details successfully entered into the database")
print("Watch count")
print("-----------")
print(watch)

print()
print("Play count")
print("----------")
print(play)

print()


