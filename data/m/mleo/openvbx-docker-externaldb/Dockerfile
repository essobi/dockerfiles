FROM ubuntu:wily  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install apache, PHP, and supplimentary programs. curl and lynx-cur are for
debugging the container.  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install apache2 libapache2-mod-
php5 php5-mysql php5-gd php-pear php-apc php5-curl curl unzip php5-curl
php5-memcache memcached build-essential wget  
  
# Enable apache mods.  
RUN a2enmod php5  
RUN a2enmod rewrite  
  
# Update the PHP.ini file, enable <? ?> tags and quieten logging.  
RUN sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php5/apache2/php.ini  
#RUN sed -i "s/error_reporting = .*$/error_reporting = E_ERROR | E_WARNING |
E_PARSE/" /etc/php5/apache2/php.ini  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ALL/"
/etc/php5/apache2/php.ini  
  
RUN sed -i "s/zlib.output_compression = Off/zlib.output_compression = On/"
/etc/php5/apache2/php.ini  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
# Download OpenVBX into /var/www/site  
RUN rm -fr /var/www/site && mkdir /var/www/site && \  
wget https://api.github.com/repos/twilio/OpenVBX/zipball/1.2.20 && \  
  
unzip 1.2.20 -d /tmp && \  
cp -a /tmp/twilio*/. /var/www/site && \  
rm -rf /tmp/twilio*  
  
COPY 000-default.conf /etc/apache2/sites-enabled/000-default.conf  
COPY run.sh ./run.sh  
  
RUN chown -R root:www-data /var/www  
RUN chmod -R 777 /var/www/site/audio-uploads var/www/site/OpenVBX/config  
  
EXPOSE 80  
CMD ./run.sh  

