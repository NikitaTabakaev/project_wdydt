from datetime import datetime


class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name_person):
        self.__name = name_person


person_1 = Person(input('Введите свое имя: '))


def add_info():
    with open('Что я сегодня делал.txt', 'a', encoding='utf-8') as file:
        file.writelines(f"{person_1.name}: {datetime.today().strftime('%d.%m.20%y')} - "
                        f"{input('Чем сегодня занимались?: ')}")


if __name__ == '__main__':
    add_info()

# Нужно будет сделать sqlite
# поля имя, дата, что делал
