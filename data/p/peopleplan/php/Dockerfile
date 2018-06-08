FROM ubuntu:precise  
MAINTAINER David Hong <david.hong@peopleplan.com.au>  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
VOLUME ["/var/www/html"]  
  
# Update takes too long at build time; will be cleaned in the final.  
RUN apt-get update  
RUN apt-get install -yq \  
apache2 \  
php5 \  
php5-cli \  
libapache2-mod-php5 \  
php5-curl \  
php5-fpm \  
php5-gd \  
php5-imagick \  
php5-ldap \  
php5-mcrypt \  
php5-mysql \  
php5-sqlite \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/* \  
&& a2enmod rewrite \  
&& a2dissite 000-default \  
&& rm /etc/apache2/sites-available/*  
  
COPY *.conf /etc/apache2/  
COPY envvars /etc/apache2/  
  
RUN service apache2 stop  
  
COPY apache2-foreground /usr/local/bin/  
WORKDIR /var/www/html  
  
EXPOSE 80  
EXPOSE 443  
CMD ["apache2-foreground"]  

