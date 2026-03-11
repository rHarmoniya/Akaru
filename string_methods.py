#string մեթոդներ

text1 = 'Hello World'
text2 = text1.strip()  # հեռացնում է բացատները սկզբից և վերջից
print(text2)
text3 = text2.upper()  # դարձնում է մեծատառ
print(text3)
text4 = text3.lower()  # դարձնում է փոքրատառ
print(text4)
text5 = text2.replace(' ','-')  # փոխարինում է բացատները "-"
print(text5)
text6 = text2.split(sep='_')  # բաժանում է "_" նշանով
print(text6)

