#! /bin/sh export PATH=$PATH:/usr/local/bin

file="/var/lib/mysql-files/weather7day.txt"
if [ -f "$file" ];then
  rm -f "$file"
fi

cd /home/by/python_test/weather/
rm weather.log
nohup scrapy crawl weather >> weather.log 2>&1 


sql_txt="select * from weather7day  into outfile '/var/lib/mysql-files/weather7day.txt' lines terminated by '\n';"
mysql -uroot -p123456 bs_db -e "${sql_txt}"

