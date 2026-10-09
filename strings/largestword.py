# LARGEST WORD
sentence = "this is a historical painting from India"
words = sentence.split()
large = max(words, key = len)
print(large)