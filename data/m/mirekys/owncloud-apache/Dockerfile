FROM debian:7  
MAINTAINER Miroslav Bauer <bauer@cesnet.cz>  
  
ADD exec.sh /exec.sh  
RUN chmod 755 /exec.sh  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update package lists and install apache2 + PHP5.4  
RUN apt-get update && apt-get install -yq wget bzip2  
RUN apt-get install -qy apache2 libapache2-mod-php5  
RUN apt-get install -qy php5 php5-curl php5-gd php5-intl php5-imagick
php5-json php5-pgsql  
  
# Install ownCloud  
RUN mkdir -p /app  
ADD https://download.owncloud.org/community/owncloud-6.0.3.tar.bz2 /  
  
WORKDIR /app/  
RUN tar xvf /owncloud-6.0.3.tar.bz2  
RUN rm /owncloud-6.0.3.tar.bz2  
RUN mkdir -p /app/owncloud/data/  
ADD conf/.htaccess /app/owncloud/data/.htaccess  
  
# Set hardened file permissions  
RUN chown -R root:root /app/owncloud  
RUN chown -R www-data:www-data /app/owncloud/config/  
RUN chown -R www-data:www-data /app/owncloud/data/  
RUN chown root:root /app/owncloud/data/.htaccess  
RUN chown -R www-data:www-data /app/owncloud/apps/  
  
# Disable and remove default sites  
RUN a2dissite default default-ssl  
RUN rm -f /etc/apache2/sites-available/*  
  
# Install owncloud siteconfig  
ADD conf/default* /etc/apache2/sites-available/  
RUN chown -R root:root /etc/apache2/sites-available/  
  
# Enable neccessary apache modules and sites  
RUN a2enmod ssl rewrite  
RUN a2ensite default default-ssl  
  
EXPOSE 443  
EXPOSE 80  
WORKDIR /  
CMD ["/exec.sh"]  

