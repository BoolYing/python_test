#! /bin/sh export PATH=$PATH:/usr/local/bin

cd /home/by/python_test/weather/
nohup scrapy crawl weather >> weather.log 2>&1 &

