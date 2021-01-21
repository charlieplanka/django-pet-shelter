# Приют для животных

Сайт вымышленного приюта с базой животных разных видов.  
На главной странице доступен список всех животных, которые находятся в приюте. Животных можно отфильтровать по виду (собаки, кошки, гуси и так далее).  

![](https://i.imgur.com/6ei3YjX.png)
  
При клике на карточку животного открывается страница с детальной информацией о питомце.  

---
Проект написан на Django. Фронт — HTML/CSS + Bootstrap. БД — PostgreSQL.

### Как развернуть 
#### Windows
1. Склонируйте репозиторий и создайте внутри папки виртуальное окружение:
```
git clone https://github.com/charlieplanka/django-pet-shelter.git
cd django-pet-shelter
virtualenv venv
```
2. Активируйте окружение и установите зависимости:
```
.\venv\Scripts\activate
pip install -r requirements.txt
```
3. Сгенерируйте секретный ключ на [Djecrety](https://djecrety.ir/).
4. Создайте файл `.env` в каталоге `\shelter` и запишите в него значение ключа:
```
Echo 'SECRET_KEY=0#*rrb+!hpo_e=bt(5w=e3(r=yige=)z$-7eccj*3z$0#4zoec' > ".\shelter\.env"
```
5. Миграции, база, фикстуры.
6. Запустите сервер (по умолчанию поднимется на 8000 порту):
```
python manage.py runserver
```

#### Linux
1. Склонируйте репозиторий и создайте внутри папки виртуальное окружение:
```
git clone https://github.com/charlieplanka/django-pet-shelter.git
cd django-pet-shelter
python3 -m venv venv
```
2. Активируйте окружение и установите зависимости:
```
source venv/bin/activate
pip install -r requirements.txt
```
3. Сгенерируйте секретный ключ на [Djecrety](https://djecrety.ir/).
4. Создайте файл `.env` в каталоге `/shelter` и запишите в него значение **сгенерированного** ключа:
```
echo 'SECRET_KEY=0#*rrb+!hpo_e=bt(5w=e3(r=yige=)z$-7eccj*3z$0#4zoec' > shelter/.env
```
5. Миграции, база, фикстуры.
6. Запустите сервер (по умолчанию поднимется на 8000 порту):
```
python manage.py runserver
```
