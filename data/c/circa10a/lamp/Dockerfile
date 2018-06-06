FROM ubuntu:16.04  
ENV HTTPD_PATH /var/www/html/  
ENV MYSQL_PW root  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 3306  
RUN echo "mysql-server-5.7 mysql-server/root_password password ${MYSQL_PW}" |
debconf-set-selections && \  
echo "mysql-server-5.7 mysql-server/root_password_again password ${MYSQL_PW}"
| debconf-set-selections && \  
apt-get update && \  
apt-get upgrade -y && \  
apt-get -y install \  
apache2 \  
mysql-server \  
php \  
libapache2-mod-php \  
php7.0-mysql \  
php7.0-curl \  
php7.0-json \  
unzip \  
wget && \  
rm -rf /var/lib/apt/lists/*  
  
VOLUME /var/lib/mysql  
  
RUN chmod -R 755 ${HTTPD_PATH} && chown -R www-data:www-data ${HTTPD_PATH}  
  
CMD service mysql start && service apache2 start && tail -f /dev/null  

