cd ../../ && python manage.py makemigrations contacts && python manage.py migrate
python manage.py createsuperuser --username %username% --email %username%@discord-friends.com
cd scripts/windows && startup.bat