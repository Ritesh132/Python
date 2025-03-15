import random

secretNo = random.randint(1, 10)
print('Choose a number between 1 and 10')

for _ in range(1, 4): 
    print('Take a guess')
    guess = int(input())

    if guess < secretNo:
        
        print('Guess is too low')
    elif guess > secretNo:
        print('Guess is too high')
    else:
        print('Correct!')
        break
if guess==secretNo:
   print('correct guess that is '+str(secretNo))
else:
    print('incorrect guess, correct number is '+str(secretNo))   