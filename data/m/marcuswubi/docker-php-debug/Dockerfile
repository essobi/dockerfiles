FROM marcuswubi/docker-php:7  
  
MAINTAINER maviniciuus <maviniciuus@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y php-xdebug multitail screen && \  
  
echo "xdebug.remote_enable=on" >> /etc/php/7.0/apache2/conf.d/20-xdebug.ini &&
\  
echo "xdebug.remote_autostart=off" >>
/etc/php/7.0/apache2/conf.d/20-xdebug.ini && \  
  
sed -i 's/^display_errors = .*/display_errors = On/'
/etc/php/7.0/apache2/php.ini && \  
sed -i 's/^error_reporting = .*/error_reporting = E_ALL \& ~E_DEPRECATED \&
~E_STRICT \& ~E_NOTICE/' /etc/php/7.0/apache2/php.ini && \  
  
rm -rf /var/lib/apt/lists/*  

