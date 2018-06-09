FROM nginx:1.10  
  
RUN set -x; \  
apt-get update && apt-get upgrade; \  
apt-get install -y php5 php5-fpm php5-gd php5-mysql php5-cli php5-common
php5-curl php5-json php5-intl \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
libxslt-dev \  
libldap2-dev \  
imagemagick \  
curl \  
git \  
subversion \  
unzip \  
wget \  
supervisor  
  
RUN set -x; \  
rm -rf /var/lib/apt/lists/*  
  
# Using www-data user  
RUN sed -i 's/user nginx/user www-data/g' /etc/nginx/nginx.conf  
  
# Setup the Composer installer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"  
  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --version=1.2.0 && rm -rf /tmp/composer-setup.php  
  

