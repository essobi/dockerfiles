# Lap  
#  
# VERSION 0.1  
FROM ubuntu:16.04  
MAINTAINER Isael Sousa <faelp22@gmail.com>  
  
# install apache2 and php  
RUN apt-get update  
RUN apt-get install php php-xml php-mysql php-pgsql php-sqlite3 php-curl
apache2 apache2-bin libapache2-mod-php -y  
RUN apt-get clean  
RUN rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# volumes  
VOLUME ["/var/www/html"]  
  
EXPOSE 80  
#ENTRYPOINT ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
CMD /usr/sbin/apache2ctl -D FOREGROUND  
  

