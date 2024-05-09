file = open("datos50.csv", "w")
for i in range(50):
    file.write(str(i)+"@correorealahra1.com"+"\n")
file.close()