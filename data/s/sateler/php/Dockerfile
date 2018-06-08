FROM debian:jessie  
  
RUN apt-get update && apt-get install -y \  
apache2-mpm-prefork \  
apache2 \  
libapache2-mod-php5 \  
php5-cli \  
php5-mysql \  
php5-mcrypt \  
php5-curl \  
php5-gd \  
php5-intl \  
&& apt-get clean  
  
RUN sed -i -e 's|^ErrorLog.*|ErrorLog /proc/self/fd/2|'
/etc/apache2/apache2.conf  
  
# Fixup for https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=822631  
ADD icu/res/libicu52_52.1-8+deb8u3.1_amd64.deb /  
RUN dpkg -i /libicu52_52.1-8+deb8u3.1_amd64.deb && rm
libicu52_52.1-8+deb8u3.1_amd64.deb  
  
ADD default /etc/apache2/sites-available/000-default.conf  
ADD mpm_prefork.conf /etc/apache2/conf.d/  
  
RUN a2ensite 000-default && a2enmod rewrite  
  
WORKDIR /var/www/  
  
CMD . /etc/apache2/envvars && exec apache2 -DFOREGROUND  
  

