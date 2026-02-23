def welcome_user():
    print('May I have your name? ', end='')
    name = input().strip()  # <-- Используем input() и strip()
    print(f'Hello, {name}!')
    return name
