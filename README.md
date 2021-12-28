# library
Для запуска и проверки приложения:
1) Скопируйте репозиторй: "git clone https://github.com/AlexanderPron/library.git"
2) Создайте новую виртуальную среду окружения: "virtualenv library"
3) Перейдите в каталог с проектом: "cd library"
4) Активируйте виртуальную среду:  ". ./Scripts/activate" или "source ./Scripts/activate"
5) Установите необходимые зависимости: "pip install -r requirements.txt"
6) Перейдите далее в каталог с приложением: "cd library" (Вы должны оказать на одном уровне с файлом manage.py)
7) Сделайте миграции: 
  a) "python manage.py makemigrations"
  b) "python manage.py migrate"
8) Импортируйте в бд данные из файла data.xml: "python manage.py loaddata data.xml" 
9) Запустите приложение: "python manage.py runserver"
10) В браузере перейдите по адресу: "http://127.0.0.1:8000/"
11) Проверьте работу

Учетные данные администратора:
login: admin
pass: skillfactory
