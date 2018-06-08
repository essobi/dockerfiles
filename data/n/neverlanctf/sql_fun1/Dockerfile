FROM richarvey/nginx-php-fpm  
  
MAINTAINER Zane Durkin <zane@zemptech.com>  
  
RUN \  
apt-get update --fix-missing && \  
apt-get install -y mysql-server  
  
# set up nginx  
RUN sed -i 's/root \/usr\/share\/nginx\/html/root \/var\/www\/html/g'
/etc/nginx/sites-enabled/default.conf  
RUN rm /var/www/html/*  
  
# create mysql password for root and set to /tmp/pass_root file  
RUN \  
export MYSQL_PASS=$(openssl rand -hex 100) && \  
echo $MYSQL_PASS > /tmp/pass_root && \  
export MYSQL_PASS=$(openssl rand -hex 100) && \  
echo $MYSQL_PASS > /tmp/pass_web  
  
# copy db.sql file  
COPY other/db.sql /tmp/db.sql  
  
# final edit db.sql file with passwords  
RUN \  
sed -i 's/<password_web>/'$(cat /tmp/pass_web)'/g' /tmp/db.sql && \  
sed -i 's/<password_root>/'$(cat /tmp/pass_root)'/g' /tmp/db.sql  
  
# set up config and import files  
COPY other/supervisord.conf /etc/  
COPY web/ /var/www/html/  
  
# set up php file with password  
RUN sed -i 's/<password_web>/'$(cat /tmp/pass_web)'/g' /var/www/html/index.php  
  
# setup database  
RUN \  
/bin/bash -c "usr/bin/mysqld_safe &" && \  
sleep 5 && \  
mysql -u root < /tmp/db.sql && \  
rm /tmp/db.sql && \  
rm /tmp/pass_web && \  
rm /tmp/pass_root  
  
  

