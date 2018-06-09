# TenantCloud Docker Image  
#  
# VERSION 0.1  
FROM ubuntu:16.04  
MAINTAINER Igor Bronovskyi <admin@brun.if.ua>  
  
ENV TERM=xterm  
  
RUN export LANG=en_US.UTF-8  
RUN export DEBIAN_FRONTEND=noninteractive  
  
RUN apt update && \  
apt upgrade -y  
  
# Added custom repositories  
RUN apt install language-pack-en -y  
RUN apt install -y --force-yes software-properties-common  
RUN apt-add-repository ppa:nginx/development -y  
RUN apt-add-repository ppa:chris-lea/redis-server -y  
RUN LC_ALL=en_US.UTF-8 apt-add-repository ppa:ondrej/apache2 -y  
RUN LC_ALL=en_US.UTF-8 apt-add-repository ppa:ondrej/php -y  
RUN apt update  
  
# Install additional Software  
RUN apt install -y --force-yes build-essential curl fail2ban gcc git
libmcrypt4 libpcre3-dev wget \  
make python2.7 python-pip sendmail supervisor ufw unattended-upgrades unzip
whois zsh  
  
RUN pip install httpie  
  
RUN echo "tenantcloud.l" > /etc/hostname  
#RUN sed -i "/127\\.0\\.0\\.1.*localhost/127.0.0.1tenantcloud.l.localdom ain
tenantcloud.l localhost/"/etc/hosts  
#RUN hostname tenantcloud.l  
RUN ln -sf /usr/share/zoneinfo/UTC /etc/localtime  
  
# Install Base PHP Packages  
RUN apt install -y --force-yes php7.1-cli php7.1-dev \  
php7.1-pgsql php7.1-sqlite3 php7.1-gd \  
php7.1-curl php7.1-memcached \  
php7.1-imap php7.1-mysql php7.1-mbstring \  
php7.1-xml php7.1-imagick php7.1-zip php7.1-bcmath php7.1-soap \  
php7.1-intl php7.1-readline php7.1-mcrypt  
  
# Install Composer Package Manager  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install software  
RUN apt install -y --force-yes nginx php7.1-fpm  
RUN openssl dhparam -out /etc/nginx/dhparams.pem 2048  
  
# Misc. PHP CLI Configuration  
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php/7.1/cli/php.ini  
RUN sed -i "s/display_errors = .*/display_errors = On/"
/etc/php/7.1/cli/php.ini  
RUN sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php/7.1/cli/php.ini  
RUN sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php/7.1/cli/php.ini  
  
# Tweak Some PHP-FPM Settings  
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i "s/display_errors = .*/display_errors = On/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i "s/;cgi.fix_pathinfo=0/cgi.fix_pathinfo=1/"
/etc/php/7.1/fpm/php.ini  
RUN sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php/7.1/fpm/php.ini  
RUN sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php/7.1/fpm/php.ini  
  
COPY php/php-xdebug.txt /root/php-xdebug.txt  
RUN cat /root/php-xdebug.txt >> /etc/php/7.1/fpm/php.ini  
  
# Install nodejs  
RUN curl --silent --location https://deb.nodesource.com/setup_6.x | bash -  
RUN apt update  
RUN apt install nodejs  
  
RUN npm install -g pm2 && \  
npm install -g gulp && \  
npm install -g yarn  
  
# Install MySQL  
COPY mysql/install-mysql.sh /root/install-mysql.sh  
COPY mysql/mysql.sql /root/mysql.sql  
RUN /root/install-mysql.sh  
  
# Install Redis  
RUN apt install -y redis-server  
  
# Install mailcatcher  
RUN apt install -y build-essential libsqlite3-dev ruby-dev  
RUN gem install mailcatcher  
RUN echo "sendmail_path = /usr/bin/env $(which catchmail) -f 'www-
data@localhost'" >> /etc/php/7.1/mods-available/mailcatcher.ini  
RUN phpenmod mailcatcher  
  
# Install Imagemagick  
RUN apt install -y imagemagick  
  
# Install xDebug  
RUN pecl install xdebug  
  
# Configure web server  
COPY ./nginx/*.conf /etc/nginx/sites-enabled/  
RUN mkdir -p /etc/nginx/ssl/tenantcloud.l  
RUN mkdir -p /etc/nginx/ssl/seleniumtc.l  
COPY ./nginx/ssl/tenantcloud.l/* /etc/nginx/ssl/tenantcloud.l/  
COPY ./nginx/ssl/seleniumtc.l/* /etc/nginx/ssl/seleniumtc.l/  
RUN chmod 777 -R /etc/nginx/ssl/  
RUN mkdir -p /var/www/tenantcloud  
  
EXPOSE 80 443 1080 3306 6001 6379 9000 9001 9090  
# Start software  
COPY supervisor/tenantcloud.conf /etc/supervisor/conf.d/  
RUN service php7.1-fpm start  
RUN service mysql start  
#RUN service redis-server start  
RUN /usr/bin/env $(which mailcatcher) --ip=0.0.0.0  
  
ENTRYPOINT ["/usr/bin/supervisord"]  
  

