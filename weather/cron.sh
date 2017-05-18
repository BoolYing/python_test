#! /bin/sh export PATH=$PATH:/usr/local/bin

cd /home/by/python_test/weather/
rm weather.log
nohup scrapy crawl weather >> weather.log 2>&1 &

