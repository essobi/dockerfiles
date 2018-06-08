FROM prosoftwares/apache-php7-letsencrypt  
MAINTAINER PR Softwares <bruno@prosoftwares.net.br>  
  
RUN apt-get update && apt-get install -y apache2 git libapache2-mod-php7.0
php7.0 php7.0-cli php-xdebug php7.0-mbstring sqlite3 php7.0-mysql php-imagick
php-memcached php-pear curl imagemagick php7.0-dev php7.0-phpdbg php7.0-gd npm
nodejs-legacy php7.0-json php7.0-curl php7.0-sqlite3 php7.0-intl wget
libsasl2-dev libssl-dev libsslcommon2-dev libcurl4-openssl-dev autoconf g++
make openssl libssl-dev libcurl4-openssl-dev pkg-config libsasl2-dev
libpcre3-dev \  
&& a2enmod headers \  
&& a2enmod rewrite \  
&& npm install -g grunt-cli bower \  
&& pecl channel-update pecl.php.net \  
  
RUN apt-get install -y php7.0-bcmath  
  
RUN echo "" > /var/www/html/index.html  
  
RUN git clone https://github.com/letsencrypt/letsencrypt  
RUN /data/letsencrypt/letsencrypt-auto --help  
  
RUN apache2ctl -D BACKGROUND  
  
EXPOSE 80 443  
CMD ["apache2ctl", "-D", "FOREGROUND"]  

