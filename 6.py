def sms(text):
    return text[:160]

text = input()
print(sms(text))
