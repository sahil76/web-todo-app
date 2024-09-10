
date = input("Enter today`s date: ")
mood = input("How do you rate your mood today from 1 - 10? ")
thoughts = input("Let your thoughts flow:\n")

with open(f"journal/{date}.txt", "w") as file:
    file.write("Mood Today - " + mood + 2*"\n")
    file.write(thoughts)