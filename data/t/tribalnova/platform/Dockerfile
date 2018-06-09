FROM tribalnova/php:53  
MAINTAINER Nicolas Degardin <ndegardin@tribalnova.com>  
  
RUN apt-get update && apt-get install -y php5-mysql mysql-client php5-memcache
php5-curl php5-sqlite sqlite3  
  
ADD files/nginx/symfony10.conf /etc/nginx/include.d/symfony.conf  
ADD files/startup-symfony10.sh /opt/docker/startup-symfony.sh  
  
RUN (perl -i -p -000 -e s@'#\\!/bin/sh'@"$(cat /opt/docker/startup-
symfony.sh|sed 's/\\\/\\\\\\\/g'|sed 's/\$/\\\\\$/g'|sed 's/\@/\\\\\@/g')"@
/opt/docker/startup.sh && rm /opt/docker/startup-symfony.sh)

