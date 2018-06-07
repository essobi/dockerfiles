FROM ubuntu:12.04  
MAINTAINER Diego Ferri <diego.ferri@looptribe.com>  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive \  
apt-get -o Dpkg::Options::="--force-confnew" install -y \  
libapache2-mod-php5 \  
apache2-mpm-itk \  
php5 \  
php5-curl \  
php5-dev \  
php5-gd \  
php5-intl \  
php5-mcrypt \  
php5-mysql \  
php5-sqlite \  
php5-xdebug \  
git \  
zip \  
curl  
  
RUN a2enmod expires && \  
a2enmod rewrite  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN adduser --uid 1000 app  
  
COPY web.ini /etc/php5/apache2/conf.d/90-web.ini  
COPY web.ini /etc/php5/cli/conf.d/90-web.ini  
  
RUN rm /etc/apache2/sites-enabled/*  
COPY vhost.conf /etc/apache2/sites-available/app.conf  
RUN a2ensite app.conf  
  
RUN curl -sS https://getcomposer.org/installer | \  
php -- --install-dir=/usr/local/bin  
  
COPY apache2-foreground /usr/local/bin/  
  
WORKDIR /home/app/app  
VOLUME /home/app/app  
RUN chown app:app /home/app/app  
  
EXPOSE 80  
EXPOSE 443  
CMD ["apache2-foreground"]

