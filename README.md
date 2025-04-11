### Описание проекта:

Yatube - учебный проект курса "backend-python" от Яндекс-Практикума.

Автор: Илья Морозов

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/VadimVolkovsky/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов к API:

Получить список всех постов (GET):
```
http://127.0.0.1:8000/api/v1/posts/
```

Получить определенный пост (GET):
```
http://127.0.0.1:8000/api/v1/posts/1/
```

Получить коментарии определенного поста (GET):
```
http://127.0.0.1:8000/api/v1/posts/1/comments/
```

Получить список всех групп (GET):
```
http://127.0.0.1:8000/api/v1/groups/
```

Создать новый пост (POST):

(Требуется аутентификация)
```
http://127.0.0.1:8000/api/v1/posts/
```
