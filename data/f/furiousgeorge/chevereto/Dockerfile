FROM php:5-apache  
MAINTAINER furiousgeorge <furiousgeorgecode@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV LC_ALL C.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV APTLIST="wget libapache2-mod-php5 php5-gd php5-curl php5-mysql"  
RUN rm /etc/apache2/mods-available/php5.load && \  
apt-get update -q && \  
apt-get install $APTLIST -qy && \  
apt-get clean && \  
rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/* /root/.cache && \  
a2enmod rewrite  
  
COPY startup.sh /startup.sh  
RUN chmod 755 /startup.sh  
  
VOLUME /var/www/html  
EXPOSE 80  
CMD ["/startup.sh"]  

