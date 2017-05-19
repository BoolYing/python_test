#! /bin/sh export PATH=$PATH:/usr/local/bin

file="/var/lib/mysql-files/weather7day_full.txt"
if [ -f "$file" ];then
  rm -f "$file"
fi

cd /home/by/python_test/today_weather/
rm weather.log
nohup scrapy crawl weather >> weather.log 2>&1 

sql_txt="select * from weather7day_full  into outfile '/var/lib/mysql-files/weather7day_full.txt' lines terminated by '\n';"
mysql -uroot -p123456 bs_db -e "${sql_txt}"

