FROM ridibooks/php:7.0  
MAINTAINER js.park@ridi.com  
  
RUN apt-get update -y  
  
# install ansible  
RUN apt-get install software-properties-common -yqq  
RUN apt-add-repository ppa:ansible/ansible -y  
RUN apt-get install ansible -yqq  
  
# install provision package  
RUN apt-get install apache2 sudo -yqq && \  
apt-get install php7.0 php-cli php-curl php-gd php-mbstring php-mcrypt \  
php-mysql libapache2-mod-php7.0 php-apcu php-intl php-imagick php-bcmath \  
php-xml php7.0-zip -yqq && \  
apt-get install zip imagemagick gifsicle jpegoptim optipng poppler-utils -yqq  
  
# install node  
RUN curl --silent --show-error https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install nodejs -yqq  
  
# enable php ext  
RUN apt-get install -y zlib1g-dev libicu-dev g++ && \  
docker-php-ext-configure intl && \  
docker-php-ext-install sockets pdo_mysql intl zip bcmath shmop && \  
pecl install xdebug && docker-php-ext-enable xdebug  
  
# install phpunit  
ADD https://phar.phpunit.de/phpunit-6.5.6.phar /usr/local/bin/phpunit  
RUN chmod +x /usr/local/bin/phpunit  

