cd ../../ && python manage.py makemigrations contacts && python manage.py migrate
python manage.py createsuperuser --username %username% --email %username%@@discord.com
cd scripts/windows && startup.bat