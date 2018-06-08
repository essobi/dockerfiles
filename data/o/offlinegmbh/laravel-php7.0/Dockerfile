FROM ubuntu:16.04  
MAINTAINER Tobias Kuendig <tobias@offline.swiss>  
  
RUN apt-get update && apt-get -y install git curl apache2 php7.0
libapache2-mod-php7.0 php7.0-mysql php7.0-sqlite php7.0-mcrypt php7.0-xml
php7.0-gd php7.0-zip unzip php7.0-mbstring php7.0-json supervisor nodejs npm
&& apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN /usr/sbin/a2enmod rewrite php7.0  
  
ADD 000-laravel.conf /etc/apache2/sites-available/  
ADD 001-laravel-ssl.conf /etc/apache2/sites-available/  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
RUN /usr/sbin/a2dissite '*' && /usr/sbin/a2ensite 000-laravel 001-laravel-ssl  
RUN /usr/sbin/a2enmod ssl  
  
RUN usermod -u 1000 www-data  
RUN groupmod -g 1000 www-data  
RUN /usr/bin/curl -sS https://getcomposer.org/installer |/usr/bin/php  
RUN /bin/mv composer.phar /usr/local/bin/composer  
RUN /bin/chown www-data:www-data -R /var/www  
  
WORKDIR /var/www  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/bin/supervisord"]  

