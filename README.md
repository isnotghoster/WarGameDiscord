# SWG

Storm War Game

Игровой бот для Discord написанный на Python.


## Требования для запуска:

1. Установить [python](https://www.python.org/downloads/) >= 3.8 вместе с PIP

2. Клонировать репозиторий ```git clone https://github.com/isnotghoster/WarGameDiscord```

3. Установить библеотеку ```pip install pycord```

4. Переименнуйте ``SWGdb.sqlite.exempel`` => ``SWGdb.sqlite``

5. Создать файл ``settings.py`` в папке ``WarGameDiscord``

6. В файл ``settings.py`` написать строку ``TOKEN =  `` [Токен вашего discord бота](https://discord.com/developers/applications)

7. Запустить главный файл ``python3 main.py``

## Настройка

###Для работы с sqlite вам потребуется: [SqliteBrowser](https://sqlitebrowser.org)

Отройте файл ``SWGdb.sqlite``: Файл -> Открыть базу данных -> В проводнике находите и открываете файл

Во вкладке ``Данные``,выбираете в списке ``Таблица: stats``

Добавляете запись,записываете нужные значения в колонки: 
1. id = Число (Если в колонке id не значения,записываете числа по порядку)
2. nation = Текст
3. type = Текст,название юнита
4. hp = Число
5. infantry_damage = Число,урон по пехоте
6. armveh_damage = Число,урон по технике
7. aircrafts_damage = Число,урон по воздушной технике
8. count_carry = Число перевозимой пехоты
9. supplie = Дробное число, если > 0 тогда прибовляет припасы,если < 0 тогда потреьляет
10. artillery = Число,дальность обстрела юнита 0 - на линии фронта, 4 - выстрел с конца на линию фронта
11. carry = Число, 0 - не может транспортировать пехоту, 1 - может транспортировать пехоту
12. cost = Число,стоимасть юнита

#### Примеры для создание новых страниц в магазине описаны в ``Cogs/Shop.py`` и ``Buttons/Shop.py``
