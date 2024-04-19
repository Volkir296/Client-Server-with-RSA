from random import randint

class RSA: # Модуль RSA для off версии

    def __init__(self):                                 # Конструктор свойств
        self.prime_one = RSA.gen_rand_prime()           # Простое № 1
        self.prime_two = RSA.gen_rand_prime()           # Простое № 2

    def gen_rand_prime(start = 1, end = 100):           # Создание простых случайных start end диапазоны чисел
        start, end = int(start), int(end)               # Преобразуем к инту на всякий
        prime = int(randint(start,end))                 # Генерация числа из диапазона
        while not RSA.is_prime(prime):
            prime = int(randint(start,end))             # Генерация числа из диапазона
        return prime

    def is_prime(n):                                    # Проверка на простое число
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def __del__(self):                                  # Деструктор
        pass

a = RSA()
print(a.prime_one,a.prime_two)