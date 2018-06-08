FROM circleci/php:7.1-browsers  
MAINTAINER Jeff Magnusson "jmagnuss@gmail.com"  
RUN sudo apt-get update  
RUN sudo apt-get install -y libmcrypt-dev git unzip wget libpng-dev libzip-dev
libsqlite3-dev libnss3 libgconf-2-4  
RUN sudo apt-get install -y libfontconfig1 chromium xvfb mysql-client  
  
# Install extra PHP modules  
RUN sudo pecl channel-update pecl.php.net  
RUN sudo pecl install zip && sudo docker-php-ext-enable zip  
RUN sudo docker-php-ext-enable xdebug  
RUN sudo docker-php-ext-install gd  
RUN sudo docker-php-ext-install bcmath  
RUN sudo docker-php-ext-install mcrypt  
RUN sudo docker-php-ext-install pdo_mysql  

