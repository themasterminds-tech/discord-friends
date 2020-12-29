username = id -un

cd ../../ && python3 manage.py makemigrations contacts && python3 manage.py migrate
python3 manage.py createsuperuser --username $username --email $username@discord-friends.com
cd scripts/mac && startup.sh
