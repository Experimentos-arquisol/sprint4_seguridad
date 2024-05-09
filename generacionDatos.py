file = open("datos210000.csv", "w")
for i in range(210000):
    file.write(str(i)+"@correorealahra1.com"+"\n")
file.close()