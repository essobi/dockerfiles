FROM ubuntu:14.04  
MAINTAINER Ygor <ygor.sif@gmail.com>  
  
# Install base packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install \  
git \  
curl \  
curl \  
sqlite3 \  
php5 \  
php5-cli \  
libapache2-mod-php5 \  
php5-mysql \  
php5-mcrypt \  
php5-gd \  
php5-memcache \  
php5-curl \  
php5-json \  
php5-apcu \  
supervisor \  
php5-sqlite \  
php5-ldap \  
php5-intl \  
php-pear \  
php5-pgsql \  
php-apc \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
COPY apache_default /etc/apache2/sites-available/default  
RUN a2enmod rewrite  
# Add image configuration and scripts  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
ENV ALLOW_OVERRIDE **True**  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
VOLUME ["/var/www"]  
EXPOSE 80  
CMD ["/run.sh"]  

