def bold(func):
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper

def italic(func):
    def wrapper():
        return f"<i>{func()}</i>"

    return wrapper

@bold
@italic
def formatted_text():
    return 'Python rocks!'

print(formatted_text())