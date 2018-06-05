FROM debian:stretch  
MAINTAINER LWB  
  
ENV REPOSITORY=GIT  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes --no-install-
recommends \  
apache2 libapache2-mod-php7.0 php7.0-mysql php7.0-gd php7.0-xml
php7.0-mbstring php7.0-zip \  
git curl ca-certificates \  
zip unzip && \  
rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN a2enmod rewrite expires actions headers alias  
  
RUN chown -R www-data:www-data /var/www  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

