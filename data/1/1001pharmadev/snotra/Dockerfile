FROM php:5.6  
RUN apt-get update && apt-get install -y \  
curl \  
ssh \  
supervisor \  
git \  
zip  
  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/run/sshd
/var/log/supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN docker-php-ext-install pdo_mysql bcmath  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
COPY php.ini /usr/local/etc/php  
COPY . /var/www/html/  
WORKDIR /var/www/html  
RUN make install-composer  
CMD ["/usr/bin/supervisord"]

