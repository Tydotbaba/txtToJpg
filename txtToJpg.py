"""
    Author: Temitayo
    Date: 29th Sept. 2019
    Description: A prython script to convert a text file to jpeg image.

"""

import binascii


print("Converting .txt file to jpg\n")

print("Begin: File conversion!\n")

#open the .txt file
f = open ("new.txt","r")

#create a new jpg file to store the image
nf = open("new.jpg","wb")
    
#Read whole file into data
while 1:
    #get a line and clean it from the .txt file
    c = f.readline()
    d = c.strip()
    d = d.strip(' ')
    d = d.replace(' ', '')
    d = d.replace('\n', '')
    if not c:
        break
    #print(c)
    #print(len(c))
    print(d)
    #print(len(d))
    nf.write(binascii.a2b_hex(bytes(d, "ascii")))

print("End: File conversion!")

# Close the file
f.close()
nf.close()
