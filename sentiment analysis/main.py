# cleaning text steps
# 1) create a tex file and take from it
# 2) convert the letter into lowercase 
# 3) remove the punctuation

import string
text = open('text.txt', encoding='utf-8').read()
lower_case = text.lower()

# str1 : Specifies the list of characters that need to be replaced.
# str2 : Specifies the list of characters with which the characters need to be replaced.
# str3 : Specifies the list of characters that needs to be deleted.
# str1 = 'abc'
# str2 = 'gef'
# returns : Returnsthe translation table which specifies the conversatios that can be used in translate() function.
print(string.punctuation)
cleaned_text = lower_case.translate(str.marketrans('', '', string.punctuation))
print(cleaned_text)