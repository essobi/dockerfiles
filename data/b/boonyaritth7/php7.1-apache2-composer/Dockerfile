FROM debian:jessie  
  
# Install base debian  
RUN apt-get update && apt-get install -y \  
wget \  
git \  
re2c \  
apt-utils \  
apt-transport-https \  
curl \  
vim \  
zip \  
lsb-release \  
build-essential  
  
RUN echo 'deb http://packages.dotdeb.org jessie all' >
/etc/apt/sources.list.d/dotdeb.list \  
&& wget https://www.dotdeb.org/dotdeb.gpg && apt-key add dotdeb.gpg && rm
dotdeb.gpg  
  
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg  
  
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
  
RUN apt-get update && apt-get -y install \  
apache2 \  
php7.1 \  
libapache2-mod-php7.1 \  
php7.1-apcu \  
php7.1-apcu-bc \  
php7.1-imagick \  
php7.1-memcached \  
php7.1-dev \  
php7.1-mongodb \  
php7.1-readline \  
php7.1-xdebug \  
php7.1-cgi \  
php7.1-fpm \  
php7.1-mysql \  
php7.1-cli \  
php7.1-json \  
php7.1-odbc \  
php7.1-redis \  
php7.1-xsl \  
php7.1-common \  
php7.1-curl \  
php7.1-mcrypt \  
php7.1-zip \  
php7.1-mbstring  
  
# Install composer  
RUN curl -sS --insecure https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Config Apache2  
RUN a2enmod rewrite  
  
# Clear Trash  
RUN rm -rf /usr/share/doc  
RUN apt-get clean && apt-get autoclean  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  
EXPOSE 80  
EXPOSE 443

