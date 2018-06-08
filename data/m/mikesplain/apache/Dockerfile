FROM ubuntu:14.04  
# Thanks to eboraas/apache for some of the details below  
MAINTAINER Mike Splain <mike.splain@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -o Dpkg::Options::='--force-confold' \--force-yes -fuy dist-upgrade &&
\  
apt-get install -yq apache2 && \  
apt-get clean  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN rm -rf /var/www/html/*  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

