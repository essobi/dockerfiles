FROM ubuntu:16.04  
MAINTAINER Ludwring Liccien <ludwring.liccien@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
# Add repository PPA php 7.1  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-get install -y build-essential make  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y language-pack-en-base &&\  
export LC_ALL=en_US.UTF-8 && \  
export LANG=en_US.UTF-8  
  
RUN DEBIAN_FRONTEND=noninteractive LC_ALL=en_US.UTF-8 add-apt-repository
ppa:ondrej/php  
  
# Update the package repository and Install base packages  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install --yes nano wget curl git vim  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install --yes nginx mcrypt  
RUN apt-get update && apt-get upgrade --yes && \  
apt-get install -y php7.1 \  
php7.1-cli \  
php7.1-common \  
php7.1-curl \  
php7.1-dba \  
php7.1-dev \  
php7.1-fpm \  
php7.1-mbstring \  
php7.1-mcrypt \  
php7.1-mysql \  
php7.1-opcache \  
php7.1-soap \  
php7.1-xml \  
php7.1-json \  
php7.1-zip \  
php-redis  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# Install Laravel Installer  
RUN composer global require "laravel/installer"  
  
# Install Node.js  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get update && \  
apt-get install -y nodejs  
  
# Install Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list && \  
apt-get update && apt-get install yarn -y  
  
# Install Ruby and gem sass and less  
RUN apt-get update && apt-get install -y ruby-full && \  
gem install sass && \  
gem install less  
  
# Install bower and grund globally  
RUN npm install -g bower gulp yarn grunt-cli  
  
# Install oci8 without internet  
RUN wget "https://s3.amazonaws.com/simonetti-tests/oci8/instantclient-sdk-
linux.x64-12.1.0.2.0.zip" -P /tmp/ && \  
wget "https://s3.amazonaws.com/simonetti-tests/oci8/instantclient-basic-
linux.x64-12.1.0.2.0.zip" -P /tmp/  
  
# Unzip them  
RUN unzip /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip -d /usr/local/ &&
\  
unzip /tmp/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /usr/local/  
  
# Install oci8  
RUN ln -s /usr/local/instantclient_12_1 /usr/local/instantclient && \  
ln -s /usr/local/instantclient/libclntsh.so.12.1
/usr/local/instantclient/libclntsh.so && \  
echo 'instantclient,/usr/local/instantclient' | pecl install oci8  
  
# Install libaio1 package needed for connecting to Oracle  
RUN apt-get update && apt-get install -y libaio1 sudo  
  
# Cleaning  
RUN apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
# Set Path for Laravel  
ENV PATH $PATH:/root/.composer/vendor/bin  
RUN echo "\n"'PATH="$PATH:/root/.composer/vendor/bin"' >> /root/.profile  
  
# Confugure php.ini  
RUN sed -ri 's/^;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g'
/etc/php/7.1/fpm/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/7.1/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/7.1/fpm/php.ini && \  
sed -i -e "s/memory_limit\s*=\s*128M/memory_limit = 1024M/g"
/etc/php/7.1/fpm/php.ini && \  
sed -i -e "s/max_execution_time\s*=\s*30/max_execution_time = 3000/g"
/etc/php/7.1/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/7.1/fpm/php-
fpm.conf && \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 200/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i -e "s/;request_terminate_timeout = 0/request_terminate_timeout =
3000/g" /etc/php/7.1/fpm/php-fpm.conf && \  
sed -i -e 's/apache/mceith/g' /etc/php/7.1/fpm/pool.d/www.conf && \  
sed -i '$a extension=oci8.so' /etc/php/7.1/fpm/php.ini  
  
# Fix ownership of sock file for php-fpm  
RUN sed -i -e "s/;listen.mode = 0660/listen.mode = 0750/g"
/etc/php/7.1/fpm/pool.d/www.conf && \  
find /etc/php/7.1/cli/conf.d/ -name "*.ini" -exec sed -i -re
's/^(\s*)#(.*)/\1;\2/g' {} \; && \  
mkdir /run/php  
  
# Confugure cli php.ini  
RUN sed -i '$a extension=oci8.so' /etc/php/7.1/cli/php.ini  
  
# Nginx site conf  
COPY default /etc/nginx/sites-available/default  
  
ADD oci8.ini /etc/php/versionPHP/mods-available/  
  
# Set user deployer  
RUN useradd -g 33 -m deployer && echo "deployer:deployer" | chpasswd &&
adduser deployer sudo  
RUN echo "deployer ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
USER deployer  
  
WORKDIR /home/deployer  
  
EXPOSE 80 443  
CMD sudo service php7.1-fpm start && \  
sudo nginx -g "daemon off;"  
  

