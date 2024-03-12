
#function to convert hours, minutes, and seconds into just seconds
def to_secs(h,m,s):
    return ((h*60*60)+(m*60)+(s))

# a series of tests to se if the function outputs the correct numbers
print(to_secs(2, 30, 10))
print(to_secs(2, 0, 0))
print(to_secs(0, 2, 0))
print(to_secs(0, 0, 42))
print(to_secs(0, -10, 10))

