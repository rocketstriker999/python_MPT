import itertools

print "\n\t\t#################################################"
print "\t\t#                                               #"
print "\t\t#                DICTONARY MAKER                #"
print "\t\t#                  BY WARLOCK                   #"
print "\t\t#                                               #"
print "\t\t#################################################"

c=raw_input("\nPLEASE ENTER CHARACHTERS [E.G Abc124&@#] BY WHICH YOU WANT TO MAKE DICTONARY :")
x=raw_input("PLEASE ENTER MAXIMUM LENGTH")
file2 =open('../../dictonary.txt','w')
res = itertools.product(c, repeat=int(x)) # 3 is the length of your result.
for i in res: 
    file2.write("\n"+''.join(i))
file2.close()
