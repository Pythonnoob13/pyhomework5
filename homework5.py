sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3', 'sandwich4', 'sandwich5', 'pastrami', 'sandwich6', 'pastrami', 'pastrami']
finished_sandwiches = []
while sandwich_orders:
    if 'pastrami' in sandwich_orders:
        print('pastrami is out of order')
    while 'pastrami' in sandwich_orders:
        sandwich_orders.remove('pastrami')
    made_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(made_sandwich)
    print(f' I made your {made_sandwich} order')
print('\nthe following sandwiches have been made')
for sandwich in finished_sandwiches:
    print( sandwich.title())



dream_vacations = {}
poll_active = True
while poll_active:

    name = input('what is your name?: ')
    question = input('If you could visit one place in the world, where would you go?: ')
    dream_vacations[name] = question
    repeat = input('whould you like poll to be continued? yes/no?: ').lower()
    if repeat == 'no':
        poll_active = False
print('\n---Poll reasuels---')
for name, vacation in dream_vacations.items():
    print(f"{name}'s dream vacation is {vacation}")