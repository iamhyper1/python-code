sentence="perfect ?  he is the perfect . perfect"
print("the original sentence is: "+sentence)
words=sentence.split()
dict1={word:sentence.count(word) for word in words}
print(dict1)