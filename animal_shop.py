
# 2) Создайте игру "Магазин животных". Реализуйте базовый класс Animal (животное) с атрибутами name (имя) и price (цена),
# а также методом sound(), который возвращает звук, издаваемый животным. От него унаследуйте классы Dog, Cat и Bird,
# каждый из которых переопределяет метод sound() для возврата соответствующего звука для каждого типа животного.
# Класс Shop должен иметь атрибуты animals (список доступных животных) и budget (бюджет магазина),
# а также методы buy_animal(animal) для покупки животного и sell_animal(animal) для продажи животного.
# Реализуйте проверки наличия достаточного бюджета у магазина для покупки и наличия животного в магазине для продажи.
class Animal:
    def __init__(self, name, price):
        self.__name = name
        if price >= 0:
            self.__price = price
        else:
            raise ValueError('Цена не может быть отрицательной')

    @property
    def name(self):
        return self.__name
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, total):
        if total >= 0:
            self.__price = total
        else:
            raise ValueError('Цена не может быть отрицательной')

    def sound(self):    
        return 'животное издаёт звук'
        

class Dog(Animal): 
    def sound(self):
        return f'{self.name} говроит гав-гав'


class Cat(Animal):
    def sound(self):
        return f'{self.name} говорит мяу-мяу'


class Bird(Animal):
    def sound(self):
        return f'{self.name} говорит чик-чирик'


class Shop():
    def __init__(self, budget, animals = None):
        self.__animals = [] if animals is None else list(animals)
        if budget < 0:
            raise ValueError('Бюджет не может быть отрицательным')
        self.__budget = budget #бюджет магазина

    @property
    def budget(self):
        return self.__budget

    @property
    def animals(self):
        return tuple(self.__animals)

    def _cheking_budget(self, animal):
        if animal.price > self.__budget:
            raise ValueError('Недостаточно средств')
        return True

    def buy_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError('Ожидаю Animal')
        else:
            if self._cheking_budget(animal):
                self.__animals.append(animal)
                self.__budget -= animal.price

    def sell_animal(self, animal):
        if animal not in self.__animals:
            raise ValueError('Не имеется такого животного')
        self.__animals.remove(animal)
        self.__budget += animal.price




first_dog = Dog('bobik', 1000)
best_shop = Shop(budget=2000)
print(f'баланс до покупки: {best_shop.budget}')
best_shop.buy_animal(first_dog)
print(best_shop.animals)
print(f'балаанс после покупки:{best_shop.budget}')
best_shop.sell_animal(first_dog)
print(f'баланс после продажи:{best_shop.budget}')
second_dog = Animal('jack', 8000)

print(isinstance(first_dog, Dog))