#! /bin/sh export PATH=$PATH:/usr/local/bin

file="/var/lib/mysql-files/weather7day_full.txt"
if [ -f "$file" ];then
  rm -f "$file"
fi

cd /home/by/python_test/today_weather/
rm weather.log
nohup scrapy crawl weather >> weather.log 2>&1 &


