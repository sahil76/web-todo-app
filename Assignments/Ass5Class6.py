
new_member = input("Enter the new member to add: ") + "\n"

file = open("../members.txt", "r")
members = file.readlines()
print(members)
file.close()
members.append(new_member)

file = open("../members.txt", "w")
file.writelines(members)
file.close()

file = open("../members.txt", "r")
print(file.read())
file.close()

