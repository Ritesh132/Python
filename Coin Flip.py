import random

def has_streak(flips, streak_length=6):
    count = 1
    for i in range(1, len(flips)):
        if flips[i] == flips[i - 1]:
            count += 1
            if count == streak_length:
                return True
        else:
            count = 1
    return False

numberOfStreaks = 0
experiments = 10000

for _ in range(experiments):
    flips = [random.choice(['H', 'T']) for _ in range(100)]
    if has_streak(flips):
        numberOfStreaks += 1

print(f'Chance of streak: {numberOfStreaks / experiments * 100:.2f}%')
