FROM debian:jessie  
MAINTAINER Hernandes Benevides de Sousa  
  
# Install from dotdeb  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 89DF5277  
RUN echo "deb http://packages.dotdeb.org jessie all" >
/etc/apt/sources.list.d/dotdeb.list  
  
# Install base packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -yq install \  
php7.0 \  
php7.0-apcu \  
php7.0-cli \  
php7.0-common \  
php7.0-curl \  
php7.0-fpm \  
php7.0-gd \  
php7.0-mysql \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
# Install Composer  
RUN php -r "readfile('https://getcomposer.org/installer');" | php \  
&& \  
mv composer.phar /usr/local/bin/composer  
  
EXPOSE 9000  
CMD ["php-fpm7.0"]  
  
COPY etc /etc  

