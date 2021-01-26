# Приют для животных

Сайт вымышленного приюта с базой животных разных видов.  
  
На главной странице доступен список всех животных, которые находятся в приюте. Животных можно отфильтровать по виду (собаки, кошки, гуси и так далее).  

![](https://i.imgur.com/iSd9VFP.png)
  
При клике на карточку животного открывается страница с детальной информацией о питомце.  
  
На странице **«Добавить объявление»** можно добавить нового питомца.  
Перед добавлением необходимо авторизоваться, либо зарегистрироваться.

---
Проект написан на Django. Фронт — HTML/CSS + Bootstrap. БД — PostgreSQL.

### Как развернуть 

✔️ Предварительно установите [PostgreSQL](https://www.postgresql.org/).

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

3. (необязательно) Сгенерируйте секретный ключ на [Djecrety](https://djecrety.ir/).
4. (необязательно) Создайте файл `.env` в каталоге `\shelter` и запишите в него значение ключа:
```
Echo 'SECRET_KEY=0#*rrb+!hpo_e=bt(5w=e3(r=yige=)z$-7eccj*3z$0#4zoec' > ".\shelter\.env"
```

5. Зайдите в консоль **postgreSQL** :
```
psql -U postgres
```
(`postgres` — имя пользователя-администратора по умолчанию)

6. Cоздайте юзера `shelter` с паролём `shelter`:
```
CREATE USER shelter WITH PASSWORD 'shelter';
```

7. Cоздайте базу `shelter` и назначьте юзера владельцем:
```
CREATE DATABASE shelter OWNER shelter;
```

8. Выйдите из консоли postgreSQL:
```
\q
```

9. Запустите миграции:
```
python manage.py migrate
```

10. Загрузите фикстуры:
```
python manage.py loaddata shelter_data.json
```

11. Запустите сервер (по умолчанию поднимется на 8000 порту):
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
3. (необязательно) Сгенерируйте секретный ключ на [Djecrety](https://djecrety.ir/).
4. (необязательно) Создайте файл `.env` в каталоге `/shelter` и запишите в него значение **сгенерированного** ключа:
```
echo 'SECRET_KEY=0#*rrb+!hpo_e=bt(5w=e3(r=yige=)z$-7eccj*3z$0#4zoec' > shelter/.env
```
5. Зайдите в консоль **postgreSQL** :
```
psql -U postgres
```
(`postgres` — имя пользователя-администратора по умолчанию)

6. Cоздайте юзера `shelter` с паролём `shelter`:
```
CREATE USER shelter WITH PASSWORD 'shelter';
```

7. Cоздайте базу `shelter` и назначьте юзера владельцем:
```
CREATE DATABASE shelter OWNER shelter;
```

8. Выйдите из консоли postgreSQL:
```
\q
```

9. Запустите миграции:
```
python manage.py migrate
```

10. Загрузите фикстуры:
```
python manage.py loaddata shelter_data.json
```

11. Запустите сервер (по умолчанию поднимется на 8000 порту):
```
python manage.py runserver
```
