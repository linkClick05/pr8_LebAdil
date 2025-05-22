python
import random  
import string  

def generate_password(length):  
    chars = string.ascii_lowercase  
    return ''.join(random.choice(chars) for _ in range(length))  

if __name__ == "__main__":  
    n = int(input("Введите длину пароля: "))  
    print("Сгенерированный пароль:", generate_password(n))  
