import random

wins = 0
losses = 0
ties = 0

while True:
    print("\nEnter your move: (r for rock, p for paper, s for scissors, q to quit)")
    playerMove = input().lower()

    if playerMove == 'q': 
        print("Thanks for playing!")
        break
    elif playerMove not in ['r', 'p', 's']:
        print("Invalid input! Please enter 'r', 'p', 's', or 'q' to quit.")
        continue

    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if playerMove == computerMove:
        print('It is a tie!')
        ties += 1
    elif (playerMove == 'r' and computerMove == 's') or \
         (playerMove == 'p' and computerMove == 'r') or \
         (playerMove == 's' and computerMove == 'p'):
        print('You win!')
        wins += 1
    else:
        print('You lose!')
        losses += 1

    print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
