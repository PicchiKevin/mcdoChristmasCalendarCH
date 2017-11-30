file = open("readme.md","w") 

file.write("# Mcdonald's Advent Calendar Spoiler\n")
file.write("I don't know if these codes are already available.    \n")

for x in range(1, 25):
	file.write("## "+ str(x) + " December : \n") 
	file.write('<img src="offers/'+str(x)+'.png" height="250">   ')
	file.write('<img src="barcodes/'+str(x)+'.svg" height="200">\n')