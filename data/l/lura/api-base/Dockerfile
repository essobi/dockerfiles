FROM php:7-apache  
  
RUN apt-get update; apt-get install -y git gettext cron wget zlib1g-dev &&
apt-get clean  
RUN docker-php-ext-install opcache mbstring pdo_mysql gettext zip  
  
RUN a2enmod rewrite  
  
RUN docker-php-ext-install bcmath  
RUN adduser user --uid 1000 --disabled-login --disabled-password --gecos ""  
RUN adduser user www-data  
RUN adduser www-data user  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"  
RUN php composer-setup.php  
RUN php -r "unlink('composer-setup.php');"  
RUN mv composer.phar /usr/local/bin/composer  
  
RUN touch /var/log/cron.log  
  
RUN mkdir /var/log/app  
RUN chown www-data:www-data /var/log/app  
  
## Add conf file  
ADD apache2.conf /etc/apache2/apache2.conf  
ADD php.ini /usr/local/etc/php/php.ini  
  
WORKDIR /var/www/html  
  
ONBUILD ARG composerlockpath="composer.lock"  
ONBUILD ARG composerjsonpath  
ONBUILD ARG srcpath="src/"  
ONBUILD ARG configpath="config/"  
ONBUILD ARG composercmd="composer install"  
ONBUILD ARG publicpath="public/"  
ONBUILD RUN echo "ADDING composer file..."  
ONBUILD RUN echo ${composerjsonpath:-$composerlockpath}  
ONBUILD ADD ${composerjsonpath:-$composerlockpath}
${composerjsonpath:-$composerlockpath}  
ONBUILD RUN echo "ADDING $srcpath"  
ONBUILD ADD $srcpath $srcpath  
ONBUILD RUN echo "ADDING $configpath"  
ONBUILD ADD $configpath $configpath  
ONBUILD RUN echo "ADDING $publicpath"  
ONBUILD ADD $publicpath public/  
ONBUILD RUN echo "RUNNING $composercmd \--no-plugins --no-scripts"  
ONBUILD RUN $composercmd \--no-plugins --no-scripts

