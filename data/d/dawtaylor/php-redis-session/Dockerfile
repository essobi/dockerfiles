FROM php:7.1-apache  
  
RUN apt-get update && \  
apt-get install unzip wget -y && \  
cd /tmp && \  
wget https://github.com/phpredis/phpredis/archive/master.zip -O phpredis.zip
&& \  
unzip -o /tmp/phpredis.zip && \  
mv /tmp/phpredis-* /tmp/phpredis && \  
cd /tmp/phpredis && \  
phpize && \  
./configure && \  
make && \  
make install && \  
mkdir -p /etc/php5/mods-available/ && \  
touch /etc/php5/mods-available/redis.ini && \  
echo extension=redis.so > /etc/php5/mods-available/redis.ini && \  
ln -s /etc/php5/mods-available/redis.ini /usr/local/etc/php/conf.d && \  
echo "session.save_handler = redis\nsession.save_path = tcp://redis/6379" >>
/usr/local/etc/php/conf.d/docker-php-ext-redis.ini && \  
apt-get remove unzip wget -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/  
  
RUN sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www\/html/'
/etc/apache2/sites-available/000-default.conf && \  
sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot \/var\/www\/html/'
/etc/apache2/sites-available/default-ssl.conf && \  
usermod -u 1000 www-data && \  
a2enmod rewrite && \  
chown -R www-data:www-data /var/www/html/  
  
WORKDIR /var/www/html  
VOLUME /var/www/html  
  
EXPOSE 80

