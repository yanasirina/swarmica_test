# Тестовое [задание](https://github.com/yanasirina/swarmica_test/blob/main/test.md) для компании Swarmica

### установка зависимотей:
```console
python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### создание файла с переменными окружения:
```console
cat .env.example > .env
```
При необходимости переопределить переменные в файле

### запуск необходимых контейнеров:
```console
docker-compose up -d 
```

### прогон миграций:
```console
python3 manage.py migrate 
```

### создание суперпользователя:
```console
python3 manage.py createsuperuser 
```

### сбор статических файлов:
```console
python3 manage.py collectstatic 
```

### запуск проекта:
```console
python3 manage.py runserver 
```
