while True:
    user_in = input('suck ya mum ye? :')
    if user_in == 'fuck ye dah':
        break;
    print(user_in)


from random import choice

dic = {
    'key':'val',
    'key1':'val1',
    'key2':'val2',
    'key3':'val3',
    'key4':'val4',
    'key5':'val5',
    'key6':'val6'
}



while True:
    user_in = input('type \'s\' to show another flashcard, type \'q\' to quit:_> ')
    if user_in == 'q':
        break
    elif user_in == 's':
        temp = choice(list(dic))
        print(temp)
        input()
        print(dic[temp])
    else:
        print(f'you typed {user_in}, which is not valid')
    