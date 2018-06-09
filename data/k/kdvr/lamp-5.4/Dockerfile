FROM debian:wheezy  
  
MAINTAINER Rik van der Kemp <rik@mief.nl>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Need wget, update and install  
RUN apt-get update && apt-get install wget -y  
  
# Adding Dotdeb for PHP 5.4 and desired PHP version  
RUN echo 'deb http://packages.dotdeb.org wheezy all' >> /etc/apt/sources.list
&& echo 'deb-src http://packages.dotdeb.org wheezy all' >>
/etc/apt/sources.list  
  
# Dotdeb requires apt key, get it and add  
RUN wget http://www.dotdeb.org/dotdeb.gpg && apt-key add dotdeb.gpg  
  
# Update repositories once again to have access to dotdeb  
RUN apt-get update  
  
RUN apt-get install -yq \  
apache2 \  
php5 \  
php5-apc \  
php5-cli \  
php5-curl \  
php5-gd \  
php5-intl \  
php5-mcrypt \  
php5-mysql \  
php5-xdebug \  
libapache2-mod-php5 \  
mysql-server  
  
# Expose sites folder for mounting  
VOLUME ["/sites"]  
  
# Adding necessary files  
ADD run.sh /run.sh  
RUN chmod +x run.sh  
  
COPY etc/apache2/apache2.conf /etc/apache2/apache2.conf  
COPY etc/php5/apache2/php.ini /etc/php5/apache2/php.ini  
COPY etc/php5/conf.d/20-apc.ini /etc/php5/conf.d/20-apc.ini  
COPY etc/php5/conf.d/20-xdebug.ini /etc/php5/conf.d/20-xdebug.ini  
  
EXPOSE 80  
CMD ["/run.sh"]

