FROM ubuntu:14.04  
ARG ROOT_DB_PASS="strangeHat!"  
ENV ROOT_DB_PASS=$ROOT_DB_PASS  
  
RUN echo "phpmyadmin phpmyadmin/dbconfig-install boolean true" | debconf-set-
selections && \  
echo "phpmyadmin phpmyadmin/app-password-confirm password $ROOT_DB_PASS" |
debconf-set-selections && \  
echo "phpmyadmin phpmyadmin/mysql/admin-pass password $ROOT_DB_PASS" |
debconf-set-selections && \  
echo "phpmyadmin phpmyadmin/mysql/app-pass password $ROOT_DB_PASS" | debconf-
set-selections && \  
echo "phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2" |
debconf-set-selections && \  
echo "mysql-server mysql-server/root_password password $ROOT_DB_PASS" | sudo
debconf-set-selections &&\  
echo "mysql-server mysql-server/root_password_again password $ROOT_DB_PASS" |
sudo debconf-set-selections  
  
RUN apt-get update && apt-get install -y \  
apache2 \  
php5 \  
mysql-server \  
php5-mysql \  
php5-json \  
unzip \  
curl \  
openssl \  
php5-mcrypt \  
sqlite3 \  
libsqlite3-dev \  
php5-sqlite \  
phpmyadmin \  
php5-curl \  
git-core  
  
RUN php5enmod mcrypt && a2enmod rewrite  
  
RUN cd /var/www && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /usr/local/bin/composer  
  
RUN cd /var/www && \  
git clone https://github.com/grycap/odisea.git && \  
cd odisea && \  
chmod -R 777 app storage vendor bootstrap/  
  
ADD conf/000-default.conf /etc/apache2/sites-available/  
  
ADD conf/apache2.conf /etc/apache2/  
  
RUN a2enmod rewrite && \  
echo "umask 000" | sudo tee -a /etc/resolv.conf && \  
service apache2 stop && \  
service mysql start && \  
mysql -u root -p$ROOT_DB_PASS < /var/www/odisea/database/migrations/tfm.sql &&
\  
sed -i "s/DB_PASSWORD=/DB_PASSWORD=$ROOT_DB_PASS/g" /var/www/odisea/.env  
  
EXPOSE 80  
CMD service mysql start && /usr/sbin/apache2ctl -D FOREGROUND  
  
#ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

