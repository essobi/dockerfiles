FROM debian:squeeze  
MAINTAINER Almad "bugs@almad.net"  
  
RUN echo "deb http://archive.debian.org/debian squeeze main" >
/etc/apt/sources.list && \  
echo "deb http://archive.debian.org/debian squeeze-lts main" >>
/etc/apt/sources.list && \  
echo "Acquire::Check-Valid-Until false;" > /etc/apt/apt.conf && \  
apt-get update && \  
apt-get -y -q install lighttpd php5-cgi php5-cli php5-curl php5-imagick
php5-mysql daemontools daemontools-run procps spawn-fcgi  
  
RUN groupadd w-dracidoupe-cz && \  
useradd w-dracidoupe-cz -g w-dracidoupe-cz && \  
groupadd wwwserver && \  
useradd lighttpd -g www-data -g wwwserver && \  
mkdir /etc/service/dracidoupe.cz && \  
mkdir -p /var/www/dracidoupe.cz/www_root/www/php/ && \  
mkdir -p /var/www/fastcgi/sockets/w-dracidoupe-cz/ && \  
chown -R w-dracidoupe-cz:wwwserver /var/www/fastcgi/sockets/w-dracidoupe-cz/  
# VOLUME ['/var/www/fastcgi/sockets']  
# VOLUME ['/var/www/dracidoupe.cz']  
  
WORKDIR /var/www/dracidoupe.cz/  

