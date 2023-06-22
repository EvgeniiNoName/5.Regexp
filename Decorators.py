def logger(old_function):
    def new_function(*args, **kwargs):
        from datetime import datetime
        name = old_function.__name__
        date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
        with open ("main.log", "a", encoding='utf-8') as f:
            f.write(f"{date}, {name}, {args, kwargs}, {old_function(*args, **kwargs)}\n")
        return old_function(*args, **kwargs)
    return new_function