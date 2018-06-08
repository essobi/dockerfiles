FROM chibanglw/docker-symfony-php7-composer:latest  
  
RUN apk --no-cache add git php7-simplexml php7-ssh2  
  
ADD /app /www/symfony/app  
  
#Add parameters.yml for Docker  
#ADD /docker/parameters.yml /www/symfony/app/config/parameters.yml  
ADD /bin /www/symfony/bin  
ADD /src /www/symfony/src  
ADD /var /www/symfony/var  
ADD /web /www/symfony/web  
ADD /composer.json /www/symfony/composer.json  
ADD /composer.lock /www/symfony/composer.lock  
  
#Add cert volume  
RUN mkdir -p /srv/lexic  
RUN chown -R www:www /srv/lexic  
  
# Add phpunit  
RUN wget https://phar.phpunit.de/phpunit.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
  
WORKDIR /www/symfony  
ENV SYMFONY_ENV=dev  
  
RUN chown -R www:www /www  
  
# Configure supervisord  
COPY docker/config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN composer install --no-interaction  
RUN chown -R www:www /www  
COPY /docker/parameters.yml /www/symfony/app/config/parameters.yml  

