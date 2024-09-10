
filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open(f"Bonus Dir/{filename}", "w")
    file.write("Hello")
    file.close()