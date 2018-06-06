FROM hongshunyang/docker-php5fpm  
MAINTAINER Hongshun Yang<yanghongshun@outlook.com>  
  
  
RUN apk add -U freeradius-radclient libjpeg jpeg-dev libmcrypt-dev libpng-dev
\  
php5-opcache php5-gd php5-mcrypt php5-mysqli php5-pdo_mysql \  
php5-pear php5-common php5-pear-mail_mime php5-json \  
&& pear install DB  
  
COPY tmpl/_etc_php5_php-fpm.conf.tmpl /etc/php5/php-fpm.conf.tmpl  
  
  
RUN dockerize -template "/etc/php5/php-fpm.conf.tmpl:/etc/php5/php-fpm.conf"  
##git clone -b production --single-branch git clone
https://hongshunyang@bitbucket.org/hongshunyang/daloradius.git  
  
##RUN chmod 644 $DALORADIUS_ROOT/library/daloradius.conf.php  

