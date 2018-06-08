FROM ubuntu:wily  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install php5 \  
php5-cgi \  
php5-cli \  
php5-common \  
php5-fpm \  
php-pear \  
php5-mysql \  
php5-curl \  
php5-dev \  
php5-gd \  
php5-mcrypt \  
php5-xmlrpc \  
curl \  
sqlite3 \  
sendmail && apt-get clean  
  
# Configure  
ADD ./start.sh /start.sh  
  
RUN chmod 755 /start.sh  
RUN php5enmod mcrypt  
RUN php5enmod curl  
  
CMD ["/bin/bash", "/start.sh"]  

