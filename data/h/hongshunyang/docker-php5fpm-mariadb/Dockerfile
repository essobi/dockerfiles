FROM hongshunyang/docker-php5fpm  
MAINTAINER Hongshun Yang<yanghongshun@outlook.com>  
  
## support phpmyadmin  
RUN apk -U add php5-json php5-opcache php5-gd php5-mcrypt php5-mysqli
php5-pdo_mysql  
  
COPY tmpl/_etc_php5_php-fpm.conf.tmpl /etc/php5/php-fpm.conf.tmpl  
  
RUN dockerize -template "/etc/php5/php-fpm.conf.tmpl:/etc/php5/php-fpm.conf"  
  

