import string

def wordmachine(word, wcounts):
   word = word.lower().strip(string.punctuation)
   if word.isalpha():
       if word in wcounts:
           wcounts[word] += 1
       else:
           wcounts[word] = 1

def main():
   wcounts = {}
   with open('alice.txt', 'r') as file:
       for line in file:
           words = line.split()
           for word in words:
               wordmachine(word, wcounts)

   with open('alice_w_counts.txt', 'w') as output_file:
       for word in sorted(wcounts.keys()):
           output_file.write(f"{word}: {wcounts[word]}\n")

main()

print("alice_w_counts.txt file created.")
