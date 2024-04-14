import sys

#function to split s, find the old character/group, swap it, and jam s back together
def replace(s,old,new):
    wds = new.join(s.split(old))
    return wds

def test(did_pass): #function for test suite
    linenum = sys._getframe(1).f_lineno #grabs caller's line number
    if did_pass:
        msg = "Test at line {0} PASSED.".format(linenum)
    else:
        msg =  ("Test at line {0} FAILED.".format(linenum))
    print(msg)

#tests defined in book
    
test(replace("Mississippi", "i", "I") == "MIssIssIppI")

s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") ==
    "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(s, "o", "a") ==
    "I lave spam! Spam is my favarite faad. Spam, spam, yum!")
#print for my peace of mind
b = replace(s, "om", "am")
print(b)

#below is my original attempt to make this function, it would fail on test 2
#because it couldn't handle multiple characters being replaced.
"""
# definition of function to replace characters in a fed in peice of text
def replace(s,old,new):
    snew = ""
    for i in range(len(s)):
        if s[i] == old:
            snew = snew + new
        else:
            snew = snew + s[i]
    return snew

"""

