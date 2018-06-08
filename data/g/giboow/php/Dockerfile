FROM php:7-apache  
  
  
RUN apt-get update  
RUN apt-get install -y g++ libicu-dev git  
RUN docker-php-ext-install intl  
  
RUN docker-php-ext-install sockets  
  
# Install PDO MySQL driver  
# See https://github.com/docker-library/php/issues/62  
RUN docker-php-ext-install mysqli pdo pdo_mysql  
  
#install mcrypt  
RUN apt-get install -y libmcrypt-dev  
RUN docker-php-ext-install mcrypt  
  
# Pour C&P et composer  
RUN apt-get install -y openssl libc-client-dev libkrb5-dev  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install ftp  
  
RUN apt-get install -y libcurl4-openssl-dev  
RUN docker-php-ext-install curl  
  
RUN apt-get install -y libxml2-dev  
RUN docker-php-ext-install dom  
  
# ext bcmath pour client RabbitMQ RUN docker-php-ext-configure bcmath  
RUN docker-php-ext-install bcmath gettext mbstring soap  
  
# Enable Apache mod_rewrite  
RUN a2enmod rewrite  
  
#add composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# add user to group for volume sharing  
RUN groupadd 1000  
RUN usermod -a -G 1000 www-data  
RUN usermod -a -G staff www-data  

