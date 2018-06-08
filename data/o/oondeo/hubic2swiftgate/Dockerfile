FROM phusion/baseimage:0.9.17  
MAINTAINER Joel Kaaberg <joel.kaberg@gmail.com>  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# Workaround a possible bug  
# https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=617856  
RUN rm -f /etc/apt/apt.conf.d/docker-gzip-indexes  
  
RUN apt-get update -y  
  
# Setup Apache  
RUN apt-get install apache2 libapache2-mod-php5 php5-curl -y  
RUN a2enmod rewrite && a2enmod ssl && a2enmod php5  
ADD apache/001-hubicgate.conf /etc/apache2/sites-enabled/001-hubicgate.conf  
  
# Setup SSL  
RUN mkdir /etc/apache2/ssl  
ADD apache/generatessl.sh /usr/local/generatessl.sh  
RUN chmod +x /usr/local/generatessl.sh  
RUN /usr/local/generatessl.sh  
  
# Setup hubic2swiftgate  
RUN cd /var/www  
RUN apt-get install unzip wget -y  
RUN wget https://github.com/oderwat/hubic2swiftgate/archive/master.zip  
RUN mkdir /var/www/hubic2swiftgate  
RUN unzip master.zip -d /var/www/hubic2swiftgate  
RUN mv /var/www/hubic2swiftgate/hubic2swiftgate-master/*
/var/www/hubic2swiftgate  
RUN rm -rf /var/www/hubic2swiftgate/hubic2swiftgate-master  
  
# Copy the hubic2swiftgate config file  
ADD config/config.php /var/www/hubic2swiftgate/config.php  
  
# Proper permissions  
RUN chmod 777 /var/www/hubic2swiftgate/cache  
RUN chown -R :www-data /var/www/hubic2swiftgate  
  
# Expose the https port for access  
EXPOSE 443  
# Start Apache  
CMD /usr/sbin/apache2ctl -D FOREGROUND

