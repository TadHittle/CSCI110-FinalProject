#chunk of code lifted from textbook to create initial file
myfile = open("pydoc.txt", "w")
myfile.write("My first file written from Python\n")
myfile.write("---------------------------------\n")
myfile.write("Hello, world!\n")
myfile.close()

#my reversal function, which reads the input file inf, breaks it into lines
#reverses it, and creats an output file which is the opposite of the input in line order
def reverser (inf, outf):
    inf = open(inf, "r")
    outf = open(outf, "w")
    f = inf.readlines()
    f.reverse()
    for everyline in f:
        outf.write(everyline)
    inf.close()
    outf.close()

#this takes thi file we created and calls the reverser function on it, spitting out our new file
reverser("pydoc.txt", "revpydoc.txt")

#this function helps print the new file    
def fprinter(name):
    mynewhandle = open(name, "r")
    while True:
        theline = mynewhandle.readline()
        if len(theline) == 0:
            break
        
        print(theline, end=" ")
    mynewhandle.close

#prints for testing and display purposes
print("file original:")
fprinter("pydoc.txt")
print(" ")
print("file reversed:")
fprinter("revpydoc.txt")
