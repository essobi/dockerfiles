FROM ubuntu:14.04  
MAINTAINER Tobias Gesellchen <tobias@gesellix.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get install -y lamp-server^ php-pear \  
&& apt-get install -y git bzip2 curl wget autoconf automake  
  
ADD ./morgue-vhost.conf /etc/apache2/sites-available/001-morgue.conf  
RUN a2ensite 001-morgue \  
&& a2dissite 000-default \  
&& a2enmod rewrite  
  
RUN cd / \  
&& git clone https://github.com/etsy/morgue \  
&& ln -s /morgue /var/www/morgue  
ADD ./development.json /morgue/config/development.json  
ADD ./install.sql /install-morgue.sql  
  
RUN service mysql start \  
&& mysqladmin create morgue \  
&& mysql < /install-morgue.sql \  
&& mysql --password=morgue -u morgue -h localhost morgue <
/morgue/schemas/postmortems.sql  
  
ADD ./run.sh /run.sh  
  
EXPOSE 80  

