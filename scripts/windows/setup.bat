cd ../../ && python manage.py makemigrations contacts && python manage.py migrate
python manage.py createsuperuser --username %username% --email %username%@discord-friends.localhost
cd scripts/windows && startup.bat