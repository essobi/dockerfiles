FROM php:7.1.0-cli  
  
MAINTAINER Deon van der Vyver <deon@creativelogic.es>  
  
RUN apt-get update && apt-get -y install zip unzip git curl php5-mcrypt
php5-json php5-mysqlnd php5-sqlite build-essential checkinstall libreadline-
gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev
libc6-dev libbz2-dev libssl-dev libffi-dev libxml2-dev libxslt1-dev python
python-pip python-dev && apt-get -y autoremove && apt-get clean && rm -rf
/var/lib/apt/lists/*  
RUN docker-php-ext-install -j$(nproc) \  
bcmath \  
mbstring \  
pdo_mysql  
  
COPY php.ini /usr/local/etc/php  
  
# Composer  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php --install-dir=/usr/bin --filename=composer \  
&& php -r "unlink('composer-setup.php');"  

