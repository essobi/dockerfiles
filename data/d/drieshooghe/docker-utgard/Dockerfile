FROM debian:jessie  
MAINTAINER Dries Hooghe <dries.hooghe@gmail.com>  
  
# Basic packages  
RUN apt-get update -y \  
&& apt-get install -y \  
wget \  
curl \  
xz-utils \  
apt-transport-https \  
lsb-release \  
ca-certificates \  
zip \  
unzip \  
rsync \  
git \  
iputils-ping \  
dnsutils \  
net-tools \  
cron \  
&& rm -rf /var/lib/apt/lists* \  
&& apt-get clean  
  
# Install Nginx  
RUN apt-get update -y \  
&& apt-get install -y \  
nginx \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install ImageMagick  
RUN apt-get update \  
&& apt-get install -y \  
pkg-config \  
libmagickwand-dev \  
imagemagick \  
build-essential \  
&&apt-get clean \  
&& rm -rf /var/lib/apt/lists*  
  
# Install Node  
RUN wget https://nodejs.org/dist/v6.10.2/node-v6.10.2-linux-x64.tar.xz  
RUN tar xvfJ node-v6.10.2-linux-x64.tar.xz -C /opt  
RUN rm node-v6.10.2-linux-x64.tar.xz  
RUN ln -s /opt/node-v6.10.2-linux-x64/bin/node /usr/bin/node  
RUN ln -s /opt/node-v6.10.2-linux-x64/bin/node /usr/local/bin/node  
RUN ln -s /opt/node-v6.10.2-linux-x64/bin/npm /usr/bin/npm  
RUN ln -s /opt/node-v6.10.2-linux-x64/bin/npm /usr/local/bin/npm  
  
# Install PHP  
RUN wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg  
RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
RUN apt-get update -y \  
&& apt-get install -y \  
php7.0 \  
php7.0-curl \  
php7.0-fpm \  
php7.0-cli \  
php7.0-mysql \  
php7.0-mbstring \  
php7.0-dom \  
php7.0-json \  
php7.0-zip \  
php7.0-xdebug \  
php-pear \  
&& pecl install imagick \  
&& phpenmod imagick \  
&& rm -rf /var/lib/apt/lists* \  
&& apt-get clean  
RUN sed -i -e "s:^.*cgi\\.fix_pathinfo=.*$:cgi.fix_pathinfo=0:g"
/etc/php/7.0/fpm/php.ini  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install PHPUnit  
RUN wget https://phar.phpunit.de/phpunit-6.1.phar  
RUN chmod +x phpunit-6.1.phar  
RUN mv phpunit-6.1.phar /usr/local/bin/phpunit  
  
# Prepare project cron jobs  
# (echo "* * * * * php /opt/drieshooghe/sayings/artisan schedule:run >>
/dev/null 2>&1")| crontab -  
# Expose ports  
EXPOSE 80  
EXPOSE 443  
# Files  
COPY files/root /  
RUN chmod +x /entrypoint.sh  
RUN chmod +x /start.sh  
  
# Prepare usage  
WORKDIR /opt  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/start.sh"]  

