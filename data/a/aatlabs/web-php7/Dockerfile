FROM ubuntu:16.04  
MAINTAINER @modernfidelity  
  
# Install base packages  
RUN apt-get clean && apt-get -y update && apt-get install -y locales curl
software-properties-common git \  
&& locale-gen en_US.UTF-8  
  
# Install PHP 7.1 & MySQL client  
RUN LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php  
RUN apt-get update  
RUN apt-get install -y --force-yes \  
php7.1 php7.1-dev php7.1-fpm \  
php7.1-bz2 php7.1-cli php7.1-common php7.1-curl php7.1-gd \  
php7.1-json php7.1-ldap php7.1-mbstring php7.1-mcrypt php7.1-mysql \  
php7.1-opcache php7.1-zip mysql-client php-xdebug php7.1-xml  
  
# Install Apache  
RUN apt-get install -y \  
libpng-dev \  
pkg-config \  
libcurl3-dev \  
apache2 \  
libapache2-mod-php7.1 \  
python-setuptools \  
wget  
# rm -rf /var/lib/apt/lists/*  
# Configure Apache & PHP  
RUN a2enmod \  
rewrite \  
vhost_alias \  
headers \  
access_compat \  
alias \  
authz_host \  
deflate \  
dir \  
expires \  
mime \  
mpm_prefork \  
php7.1 \  
ssl \  
proxy \  
proxy_http \  
proxy_connect  
COPY config/php.ini /etc/php7.1/apache2/php.ini  
#COPY config/apache2.conf /etc/apache2/apache2.conf  
COPY config/000-default.conf /etc/apache2/sites-available/000-default.conf  
COPY config/mpm_prefork.conf /etc/apache2/mods_available/mpm_prefork.conf  
  
# Enable PHP modules  
RUN phpenmod mcrypt pdo_mysql  
  
# Install Composer for PHP 7.1  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN touch /var/log/php_errors.log  
RUN chown www-data:www-data /var/log/php_errors.log  
RUN chmod g+rw /var/log/php_errors.log  
  
# xdebug config.  
RUN echo 'xdebug.show_error_trace=1' >> /etc/php/7.1/mods-available/xdebug.ini  
RUN echo 'xdebug.remote_port=9000' >> /etc/php/7.1/apache2/php.ini  
RUN echo 'xdebug.remote_enable=1' >> /etc/php/7.1/apache2/php.ini  
RUN echo 'xdebug.idekey="PHPSTORM"' >> /etc/php/7.1/apache2/php.ini  
RUN echo 'xdebug.remote_connect_back=0' >> /etc/php/7.1/apache2/php.ini  
RUN echo 'xdebug.remote_host=10.254.254.254' >> /etc/php/7.1/apache2/php.ini  
  
# Document that the service listens on port 80  
EXPOSE 80  

