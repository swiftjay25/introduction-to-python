playing = True
answer = 30
guesses = 5
print('''
We will be playing a guessing game - You will guess a number between 1 and 100, I will tell you if you are too high or too low, You have 5 guesses in total
''')

while playing:
    guess = input ('You have {0} guesses left, please enter your guess '.format (guesses))
    if guess == answer:
        print ("you won, the answer was {0}".format(answer))
        playing = False
    if guess<answer:
        print ('too low')
        guesses = guesses - 1
    if guess > answer:
        print ('too high')
        guesses = guesses - 1
    if guesses <=0:
        print ('you lost')
        playing = False