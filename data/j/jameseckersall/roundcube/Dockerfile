FROM jameseckersall/docker-centos-base  
  
MAINTAINER James Eckersall <james.eckersall@gmail.com>  
  
RUN yum -y install roundcubemail php-mysql  
  
COPY supervisord.d/ /etc/supervisord.d/  
COPY config.inc.php /etc/roundcubemail/  
COPY roundcubemail.conf /etc/httpd/conf.d/  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php.ini  
RUN chgrp 48 /etc/roundcubemail/config.inc.php  
  
# use this to generate des_key in config.inc.php  
RUN echo "\$config['des_key']='`cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold
-w 24 | head -n 1`';" > /etc/roundcubemail/des_key.inc.php  
  
ENV DB_USER=roundcube \  
DB_PASS=roundcube \  
DB_HOST=mysql \  
DB_NAME=roundcube \  
DEFAULT_HOST=ssl://localhost:993 \  
SMTP_SERVER=tls://localhost:25 \  
SMTP_USER='%u' \  
SMTP_PASS='%p'  
EXPOSE 80  

