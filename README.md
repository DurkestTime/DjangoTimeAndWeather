
# Django time and weather site

Простой сайт для показа информации о времени и погоде. Настраиваемый через админ панель.


## Установка

Для корректной работы требуется использовать `.venv`

Установка зависемостей
```bash
pip install -r requirements.txt
```
Настройка переменных окружения `.env`
```bash
OPENWEATHER_API_KEY=ваш_ключ_от_openweathermap
SECRET_KEY=ваш_секретный_ключ_django
```
Подготовка базы данных
```bash
python manage.py migrate
```
Запуск сервера
```bash
python manage.py runserver
```