#! /bin/sh export PATH=$PATH:/usr/local/bin

file="/var/lib/mysql-files/weather7day_full.txt"
if [ -f "$file" ];then
  rm -f "$file"
fi

file1="/var/lib/mysql-files/user_info.txt"
if [ -f "$file1" ];then
  rm -f "$file1"
fi


cd /home/by/python_test/today_weather/
rm weather.log
nohup scrapy crawl weather >> weather.log 2>&1 

sql_txt="select * from weather7day_full  into outfile '/var/lib/mysql-files/weather7day_full.txt' lines terminated by '\n';"
mysql -uroot -p123456 bs_db -e "${sql_txt}"

sql_txt1="select * from user_info  into outfile '/var/lib/mysql-files/user_info.txt' lines terminated by '\n';"
mysql -uroot -p123456 bs_db -e "${sql_txt1}"

