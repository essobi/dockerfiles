FROM ubuntu:16.04  
# fix the bash  
RUN ln -snf /bin/bash /bin/sh  
  
# Install packages  
RUN apt-get update && apt-get install -my \  
vim \  
supervisor \  
curl \  
wget \  
git \  
zip \  
bzip2 \  
php7.0-bcmath \  
php7.0-cli \  
php7.0-curl \  
php7.0-fpm \  
php7.0-gd \  
php7.0-mcrypt \  
php7.0-mbstring \  
php7.0-mysqlnd \  
php7.0-soap \  
php7.0-xml \  
php7.0-zip \  
php7.0-bcmath  
  
# Remove unused packages  
RUN apt-get autoremove -y  
  
# Add some color to vim  
RUN printf "color desert" > /root/.vimrc  
  
# Get Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Get phpMyAdmin  
RUN mkdir -p /var/www/phpmyadmin  
WORKDIR /var/www/phpmyadmin  
RUN wget https://github.com/phpmyadmin/phpmyadmin/archive/RELEASE_4_7_5.tar.gz  
RUN tar xvzf RELEASE_4_7_5.tar.gz --strip-components=1  
RUN rm RELEASE_4_7_5.tar.gz  
RUN composer update --no-dev  
RUN mkdir /var/www/phpmyadmin/sessions  
RUN chown -R www-data:www-data /var/www/phpmyadmin  
WORKDIR /  
  
# Add configuration files  
COPY conf/supervisord.conf /etc/supervisor/conf.d/  
COPY conf/php.ini /etc/php/7.0/fpm/conf.d/40-custom.ini  
COPY conf/php-fpm-www.conf /etc/php/7.0/fpm/pool.d/www.conf  
  
# Add the phpMyAdmin config file  
COPY conf/config.inc.php /var/www/phpmyadmin  
  
# Initialize the PHP FPM pid file so Supervisor can find it  
RUN service php7.0-fpm start  
  
# Move the start file  
COPY start.sh /bin/original_start.sh  
RUN tr -d '\r' < /bin/original_start.sh > /bin/start.sh  
RUN chmod -R 700 /bin/start.sh  
  
EXPOSE 9000  
ENV TERM xterm  
  
CMD ["sh", "/bin/start.sh"]

