# !/usr/bin/env bash
sudo apt update && sudo apt install python3-pip python3-dev libpq-dev nginx git
# Stop any instance of our application running currently
killall python
# change directory into folder where application is downloaded
cd Django-Weather-App-/
# Install application dependencies
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip3 install django
pip3 install django-sslserver

openssl req -x509 -newkey rsa:4096 -nodes -keyout privatekey.pem -out cert.pem -days 365 -subj "/C=IE/ST=Leinster/L=Dublin/O=National College of Ireland/OU=School of Computing/CN=ncirl.ie"
# Start the application with the process name weather_app using pm2
python manage.py runsslserver 0.0.0.0:8443 --certificate cert.pem --key privatekey.pem > /dev/null 2>&1 &