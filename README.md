# selenium構築
```
docker-compose up -d
```

```
#docker に接続する
docker exec -it webnium_app_1 /bin/bash

# プロジェクトに移動
cd /home/python_django/webnium

#マイグレート
python manage.py migrate

#webサーバー立ち上げ
python3 manage.py runserver 0:8000

```

フロント側→http://localhost:8000/
phpMyAdmin →　http://localhost:13306/