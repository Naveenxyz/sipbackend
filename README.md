# sipbackend
Django backend for SIP

git clone https://github.com/Naveenxyz/sipbackend.git
cd sipbackend
virtualenv venv -p python3
source ./venv/bin/activate
pip install -r req.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver ip:port
