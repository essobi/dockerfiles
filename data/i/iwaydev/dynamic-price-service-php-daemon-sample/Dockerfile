FROM php:7.1-cli  
  
WORKDIR /var/www/dynamic-price-service  
  
RUN apt-get clean  
RUN apt-get update  
  
# Apt-utils  
RUN apt-get install -y apt-utils  
  
RUN docker-php-ext-install sockets  
  
# Redis  
RUN pecl install redis && \  
docker-php-ext-enable redis  
  
RUN apt-get install -y wget ca-certificates && \  
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key
add - && \  
apt-get update -y  
  
RUN apt-get install -y libpq-dev && \  
docker-php-ext-install pdo_pgsql && \  
docker-php-ext-enable pdo_pgsql  
  
# Intl  
RUN apt-get install -y libicu-dev && \  
docker-php-ext-install intl  
  
# Curl  
RUN apt-get install -y libcurl4-gnutls-dev && \  
docker-php-ext-install curl  
  
# Json  
RUN docker-php-ext-install json  
  
# Mbstring  
RUN docker-php-ext-install mbstring  
  
# Gettext  
RUN docker-php-ext-install gettext  
  
# Xdebug  
RUN pecl install xdebug && \  
docker-php-ext-enable xdebug  
  
# Imagick  
RUN apt-get install -y libmagickwand-dev libmagickcore-dev && \  
pecl install imagick && \  
docker-php-ext-enable imagick  
  
# Git  
RUN apt-get install -y git  
  
# Wget  
RUN apt-get install -y wget  
  
# Bcmath  
RUN docker-php-ext-install bcmath && \  
docker-php-ext-enable bcmath  
  
# GD  
RUN apt-get install -y libpng-dev && \  
docker-php-ext-install gd && \  
docker-php-ext-enable gd  
  
# Zip  
RUN apt-get install -y unzip && \  
docker-php-ext-install zip && \  
docker-php-ext-enable zip  
  
# Amqp  
RUN apt-get install -y aptitude  
RUN aptitude update  
RUN aptitude install -y php-amqplib  
RUN apt-get install -y libssh-dev  
RUN apt-get install -y librabbitmq-dev  
RUN pecl install amqp  
RUN docker-php-ext-enable amqp  
  
# Composer  
WORKDIR /tmp  
COPY ./composer_install.sh /tmp/composer_install.sh  
RUN chmod 777 composer_install.sh  
RUN ./composer_install.sh  
  
WORKDIR /var/www/dynamic-price-service  
  
RUN apt-get autoremove && apt-get clean  
  
CMD ["php", "./yii", "sample-daemon/index"]  
HEALTHCHECK CMD ps -aux | grep "[p]hp ./yii sample-daemon" || exit 1  

