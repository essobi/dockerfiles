FROM wordpress:4.7.2-apache  
MAINTAINER phonoloop <phonoloop@spaceape.be>  
  
# VHOST change  
COPY ./vhost.conf /etc/apache2/sites-available/vhost.conf  
RUN a2dissite 000-default.conf \  
&& a2ensite vhost.conf  
  
# Install Composer  
RUN curl -s http://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Install Xdebug  
RUN pecl install xdebug-2.5.0 \  
&& docker-php-ext-enable xdebug

