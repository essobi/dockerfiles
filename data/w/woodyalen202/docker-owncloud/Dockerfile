FROM ubuntu:14.04  
MAINTAINER lucienchu<lucienchu@hotmail.com>  
  
ENV RAW_PORT=5000 \  
RAW_ADMIN="admin" \  
RAW_PASSWORD="owncloud" \  
RAW_DB_USER="root" \  
RAW_DB_PASS="5xlovemysql" \  
RAW_DB_PORT=3306 \  
RAW_DB_HOST="127.0.0.1" \  
RAW_DB_NAME="owncloud" \  
OWN_CLOUD_USER="www-data"  
  
RUN echo "Asia/Shanghai" > /etc/timezone;dpkg-reconfigure -f noninteractive
tzdata \  
# && sed -Ei
'1,$s/http:\/\/archive.ubuntu.com\/ubuntu\//http:\/\/cn.archive.ubuntu.com\/ubuntu\//g'
/etc/apt/sources.list \  
&& apt-get update -q \  
&& apt-get upgrade -y \  
  
&& apt-get install -y curl \  
&& curl
https://download.owncloud.org/download/repositories/9.1/Ubuntu_14.04/Release.key
| apt-key add - \  
&& echo 'deb
http://download.owncloud.org/download/repositories/9.1/Ubuntu_14.04/ /' >>
/etc/apt/sources.list.d/owncloud.list \  
  
&& apt-get update -q \  
&& apt-get install -y -d owncloud \  
&& echo 'mysql-server-5.5 mysql-server/root_password password 5xlovemysql' |
debconf-set-selections \  
&& echo 'mysql-server-5.5 mysql-server/root_password_again password
5xlovemysql' | debconf-set-selections \  
&& apt-get install -y owncloud  
  
VOLUME /data  
WORKDIR /var/www/owncloud  
  
COPY owncloud.conf /etc/apache2/sites-available/  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY crontab /etc/cron.d/  
  
RUN rm -rf /etc/apache2/sites-enabled/* \  
&& ln -s /etc/apache2/sites-available/owncloud.conf /etc/apache2/sites-
enabled/ \  
&& echo "ServerName 0.0.0.0" >> /etc/apache2/apache2.conf \  
&& chown -R www-data:www-data /var/www/owncloud/  
  
# create owncloud database  
#RUN service mysql start \  
# && /bin/bash +x /usr/local/bin/owncloud.sh  
  
# install owncloud  
#RUN sudo -u www-data php occ maintenance:install --database "sqlite"
\--admin-user "admin" \--admin-pass "owncloud"  
#RUN sudo -u www-data php occ maintenance:install --database "mysql"
\--database-name "owncloud" \--database-user "root" \--database-pass
"5!lovemysql" \--admin-user "admin" \--admin-pass "owncloud"  
  
#EXPOSE 5000  
  
ENTRYPOINT ["docker-entrypoint.sh"]

