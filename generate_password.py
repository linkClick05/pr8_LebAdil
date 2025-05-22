python
def generate_password(length):  
    chars = string.ascii_letters  # Добавлен верхний регистр  
    return ".join(random.choice(chars) for _ in range(length))  
