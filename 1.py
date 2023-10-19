def counter(text):
    vovels = 'уеаоёэяию'
    consonant = 'йцкнгшщзхъфвпрлджчсмтьб'

    vovels_result = 0
    consonant_result = 0

    text = text.lower()

    for letter in text:
        if letter in vovels:
            vovels_result += 1
        elif letter in consonant:
            consonant_result += 1

    print(f'Vovels: {vovels_result}')
    print(f'Consonant: {consonant_result}')


text = input('Type in the text:')
counter(text)
