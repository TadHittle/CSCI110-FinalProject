
#block of code to set up punctuation removal function
import string

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

#block of text used: Dr.evil therapy monolouge from austin powers
dr_evil = """

My childhood was typical. Summers in Rangoon, luge lessons.
In the spring, we’d make meat helmets.
When I was insolent, I was placed in a burlap bag and beaten with reeds
pretty standard, really. At the age of twelve, I received my first scribe.
At the age of fourteen, a Zoroastrian named Vilma ritualistically shaved my testicles.
At the age of 18, I went off to evil medical school.
At the age of 25, I took up tap dancing.
I wanted to be a quadruple threat, an actor, dancer… """

#a few variables and the call of the punctuation function
wds = remove_punctuation(dr_evil).split()

ecnt = 0
wcnt = 0

#ecount generator
for word in wds:
    if 'e' in word:
        ecnt += 1
#wordcount generator
for word in wds:
    wcnt += 1

epc = (ecnt/wcnt*100)


#my very overcomplicated print that took me way to long to figure out
print("Your text contains",wcnt,"words, of which",ecnt,"(" + '%.3g' % epc + "%)","contain an \"e\".")
