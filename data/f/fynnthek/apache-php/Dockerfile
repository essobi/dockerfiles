FROM debian:jessie  
MAINTAINER Fynn Kluckas <fynn.kluckas@eudahosting.de>  
  
RUN apt-get update && \  
apt-get install --fix-missing && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
apache2 \  
libapache2-mod-php5 \  
php5-mysql \  
php5-sqlite \  
php5-mcrypt \  
php5-gd \  
php5-curl \  
curl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN /usr/sbin/php5enmod mcrypt  
RUN /usr/sbin/a2enmod headers  
RUN /usr/sbin/a2enmod rewrite  
  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
RUN mkdir -p /app && rm -fr /var/www/html && ln -s /app /var/www/html  
ADD sample/ app/  
  
EXPOSE 80  
WORKDIR /app  
CMD ["/run.sh"]

