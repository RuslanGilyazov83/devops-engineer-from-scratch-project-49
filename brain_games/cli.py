import prompt


def welcome_user():
    """Запрашивает имя пользователя и приветствует его."""
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    return name
