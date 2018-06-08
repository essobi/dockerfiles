FROM debian:8.2  
ENV PHPMYADMIN_VERSION 4.5.2  
RUN apt-get update  
  
RUN \  
echo "mysql-server mysql-server/root_password password root" | debconf-set-
selections; \  
echo "mysql-server mysql-server/root_password_again password root" | debconf-
set-selections  
  
RUN \  
apt-get install -y supervisor vim curl wget; \  
apt-get install -y nginx php5-fpm mysql-server php5-mysql php5-gd php5-curl  
  
RUN \  
wget -P /tmp
https://files.phpmyadmin.net/phpMyAdmin/${PHPMYADMIN_VERSION}/phpMyAdmin-${PHPMYADMIN_VERSION}-english.tar.gz;
\  
tar -xvf /tmp/phpMyAdmin-${PHPMYADMIN_VERSION}-english.tar.gz -C /tmp; \  
rm /tmp/phpMyAdmin-${PHPMYADMIN_VERSION}-english.tar.gz; \  
mv /tmp/phpMyAdmin-${PHPMYADMIN_VERSION}-english /tmp/phpmyadmin  
  
RUN \  
useradd -g www-data nginx; \  
useradd -g www-data php-fpm; \  
useradd supervisor  
  
RUN \  
rm /var/log/mysql.log; \  
rm /var/log/mysql.err  
  
RUN ln -s /etc/nginx/sites-available/scoat /etc/nginx/sites-enabled/scoat  
  
WORKDIR /var/www/html/website  
  
CMD ["/bin/bash", "/tmp/startup.sh"]  

