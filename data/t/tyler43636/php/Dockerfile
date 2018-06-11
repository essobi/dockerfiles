FROM ubuntu:trusty  
  
MAINTAINER tyler43636@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN echo 'APT::Install-Recommends 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo 'APT::Install-Suggests 0;' >> /etc/apt/apt.conf.d/01norecommends \  
&& echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale \  
&& locale-gen en_US.UTF-8 \  
&& apt-get update \  
&& apt-get install -y ca-certificates software-properties-common curl \  
&& echo "deb http://ppa.launchpad.net/ondrej/php5-5.6/ubuntu trusty main" >
/etc/apt/sources.list.d/ondrej-php5-5_6-trusty.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 4F4EA0AAE5267A6C \  
&& apt-get update \  
&& apt-get install -y \  
php5 \  
php5-cli \  
php5-mysqlnd \  
php5-pgsql \  
php5-sqlite \  
php5-apcu \  
php5-json \  
php5-curl \  
php5-gd \  
php5-gmp \  
php5-imap \  
php5-mcrypt \  
php5-redis \  
php5-readline \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod +x /usr/local/bin/composer \  
&& rm -rf /var/lib/apt/lists/* \  
&& mkdir /etc/apache2/logs \  
&& rm -rf /etc/apache2/sites-enabled/*  
  
RUN sed -i "s/error_reporting = .*/error_reporting = E_ALL/"
/etc/php5/cli/php.ini \  
&& sed -i "s/display_errors = .*/display_errors = On/" /etc/php5/cli/php.ini \  
&& sed -i "s/memory_limit = .*/memory_limit = 512M/" /etc/php5/cli/php.ini \  
&& sed -i "s/;date.timezone.*/date.timezone = UTC/" /etc/php5/cli/php.ini  
  
COPY apache2-foreground /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/apache2-foreground  
  
COPY apache2.conf /etc/apache2/apache2.conf  
  
COPY site.conf /etc/apache2/sites-enabled/site.conf  
  
COPY php.ini /etc/php5/apache2/php.ini  
  
WORKDIR /srv  
  
EXPOSE 80  
CMD ["apache2-foreground"]  

