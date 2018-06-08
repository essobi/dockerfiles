FROM debian:jessie  
MAINTAINER Matthew Neel <matt@mrneel.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV APACHE_HTTPD "exec /usr/sbin/apache2"  
RUN apt-get -qq update  
RUN echo mysql-server mysql-server/root_password password rachel | debconf-
set-selections && \  
echo mysql-server mysql-server/root_password_again password rachel | debconf-
set-selections && \  
apt-get -y install apache2 libapache2-mod-proxy-html libxml2-dev \  
php5-common libapache2-mod-php5 php5-cgi php5 \  
mysql-server mysql-client php5-mysql  
RUN apt-get clean  
  
VOLUME ["/var/www", "/etc/apache2/sites-available", "/etc/apache2/sites-
enabled", "/var/www/modules"]  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

