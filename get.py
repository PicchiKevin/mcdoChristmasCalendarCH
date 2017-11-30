file = open("readme.md","w") 

file.write("# Mcdonald's Advent Calendar Spoiler")

for x in range(1, 25):
	file.write("## "+ str(x) + " December : \n") 
	file.write("!["+str(x)+"Dec](offers/"+str(x)+".png)  \n") 
	file.write("!["+str(x)+"Dec](barcodes/"+str(x)+".svg)\n")
