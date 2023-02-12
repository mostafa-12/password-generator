import random
import string
def generat(number):
    Upper_len=int(round(number*(20/100)))
    digits_len=int(round(number*(20/100)))
    punc_len=int(round(number*(20/100)))
    Lower_len=number-(Upper_len*3)
    Upper_case=random.choices(list(string.ascii_uppercase),k=Upper_len)
    Lower_case=random.choices(list(string.ascii_lowercase),k=Lower_len)
    digits=random.choices(list(string.digits),k=digits_len)
    punc=random.choices(list(string.punctuation),k=punc_len)
    String=[Upper_case,Lower_case,punc,digits]
    tmp=""
    for chars in String:
        for char in chars:
            tmp=tmp+char
    password=list(tmp)
    
    for i in range(number):
        random.shuffle(password)
    return password

print(generat(7))
