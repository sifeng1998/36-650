# Question 2
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

msp_str="Hello in 36-650,& other MSP courses."

# set a delete punctuation string to be null
# then save characters without punctuations in it
del_punc = ""

for word in msp_str:
    if word not in punctuations:
        del_punc = del_punc + word

print(del_punc)