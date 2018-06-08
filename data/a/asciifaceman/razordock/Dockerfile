# RazorDock for RazorCMS  
#  
# VERSION 0.2  
# use debian jessie - just because  
FROM debian:jessie  
  
MAINTAINER Charles Corbett <nafredy@gmail.com> version: 0.2  
# Update  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
apt-get -y install git apache2 libapache2-mod-php5 php5-json php5-sqlite
php5-curl php5-gd php-pear php-apc curl php5-xmlrpc unzip  
  
RUN apt-get upgrade -y  
  
# Enable rewrite  
RUN a2enmod rewrite  
  
# Set timezone  
RUN echo US/Pacific > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
# Copy RazorCMS into the container  
ADD files/razorCMS-3.4.6 /razorcms  
  
# Add apache config  
ADD ./001-razorCMS.conf /etc/apache2/sites-available/  
RUN ln -s /etc/apache2/sites-available/001-razorCMS.conf /etc/apache2/sites-
enabled/  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
  
# ENV variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_SERVERADMIN admin@localhost  
ENV APACHE_SERVERNAME localhost  
ENV APACHE_SERVERALIAS docker.localhost  
ENV APACHE_DOCUMENTROOT /razorcms  
  
# expose 80  
EXPOSE 80  
ADD start.sh /start.sh  
RUN chmod 0755 /start.sh  
RUN chown -R www-data:www-data /razorcms  
CMD ["bash", "start.sh"]

