# !/usr/bin/env bash
sudo apt update && sudo apt install nodejs npm
# Install pm2 which is a production process amanger for Node.js with a built-in load balancer.
sudo npm install -g pm2
# Stop any instance of our application running currently
pm2 stop weather_app
# change directory into folder where application is downloaded
cd WeatherApp/
# Install application dependencies
npm install
# Start the application with the process name weather_app using pm2
pm2 start ./bin/www -- name weather_app