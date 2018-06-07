FROM ubuntu:16.04  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends software-properties-common  
RUN LC_ALL=C.UTF-8 apt-add-repository -y ppa:ondrej/php  
RUN LC_ALL=C.UTF-8 apt-add-repository -y ppa:ondrej/apache2  
RUN apt-key update  
RUN apt-get update  
RUN apt-get install -y \  
php7.2 \  
php7.2-apcu \  
php7.2-cli \  
php7.2-common \  
php7.2-curl \  
php7.2-fpm \  
php7.2-gd \  
php7.2-gmp \  
php7.2-imagick \  
php7.2-intl \  
php7.2-json \  
php7.2-mbstring \  
php7.2-mongo \  
php7.2-mysql \  
php7.2-readline \  
php7.2-redis \  
php7.2-soap \  
php7.2-sqlite \  
php7.2-tidy \  
php7.2-xdebug \  
php7.2-xml \  
php7.2-xmlrpc \  
php7.2-zip \  
apache2 \  
libapache2-mod-php7.2 \  
unzip \  
libimage-exiftool-perl \  
imagemagick \  
git  
  
RUN ln -sf /dev/stderr /var/log/apache2/error.log  
RUN ln -sf /dev/stdout /var/log/apache2/access.log  
RUN ln -sf /dev/stdout /var/log/apache2/other_vhosts_access.log  
RUN a2dismod mpm_event && a2enmod mpm_prefork  
RUN a2enmod rewrite  
RUN a2enmod ssl  
RUN a2enmod http2  
RUN a2enmod expires  
RUN a2enmod headers  
RUN rm /etc/apache2/sites-enabled/*  
RUN mv /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-
available/050-default.conf  
RUN mv /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-
available/050-default-ssl.conf  
RUN a2ensite 050-default  
RUN a2ensite 050-default-ssl  
RUN update-alternatives --set php /usr/bin/php7.2  
RUN apache2ctl configtest  
RUN phpdismod -s cli xdebug  
  
ADD composer-setup.sh /  
RUN chmod +x composer-setup.sh  
RUN /composer-setup.sh  
  
EXPOSE 80  
EXPOSE 443  
ADD start.sh /  
RUN chmod +x start.sh  
  
CMD ["/start.sh"]  
  

