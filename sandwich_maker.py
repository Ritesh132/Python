import pyinputplus as pyip

def sandwich_maker():
    prices = {
        'bread': {'wheat': 1.5, 'white': 1.0, 'sourdough': 2.0},
        'protein': {'chicken': 3.0, 'turkey': 3.5, 'ham': 2.5, 'tofu': 2.0},
        'cheese': {'cheddar': 1.0, 'swiss': 1.5, 'mozzarella': 1.2},
        'extras': {'mayo': 0.5, 'mustard': 0.5, 'lettuce': 0.3, 'tomato': 0.4}
    }
    
    print("Welcome to the Sandwich Maker!")
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt="Choose your bread:\n", numbered=True)
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt="Choose your protein:\n", numbered=True)
    
    cheese_want = pyip.inputYesNo("Do you want cheese? (yes/no)\n")
    cheese_type = ''
    if cheese_want == 'yes':
        cheese_type = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], prompt="Choose your cheese:\n", numbered=True)
    
    extras_want = pyip.inputYesNo("Do you want mayo, mustard, lettuce, or tomato? (yes/no)\n")
    extras_total = 0
    if extras_want == 'yes':
        for extra in ['mayo', 'mustard', 'lettuce', 'tomato']:
            add_extra = pyip.inputYesNo(f"Do you want {extra}? (yes/no)\n")
            if add_extra == 'yes':
                extras_total += prices['extras'][extra]
    
    num_sandwiches = pyip.inputInt("How many sandwiches would you like?\n", min=1)
    
    total_cost = (prices['bread'][bread] + prices['protein'][protein] + (prices['cheese'].get(cheese_type, 0)) + extras_total) * num_sandwiches
    print(f"Total cost: ${total_cost:.2f}")

sandwich_maker()
