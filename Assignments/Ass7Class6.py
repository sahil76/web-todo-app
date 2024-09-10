
import os

for i in os.listdir('../Misc'):
    file = open(f"./Misc/{i}", "r")
    print(file.read())
    file.close()
