FROM debian:8.5  
MAINTAINER Raphaël Snts <r@snts.io>  
  
EXPOSE 80 7331  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install Apache  
RUN apt-get -y install apache2  
  
# Install PHP  
RUN apt-get -y install php5 php-pear php5-curl php5-gd php5-xmlrpc php5-intl
php5-pgsql  
  
# Install ssh  
RUN apt-get -y install openssh-server  
  
# Install other stuff  
RUN apt-get -y install git pwgen vim  
  
# Git clone Moodle 3.1  
RUN rm -rf /var/www/html  
RUN git clone -b MOODLE_31_STABLE git://git.moodle.org/moodle.git
/var/www/html  
RUN chown -R www-data:www-data /var/www/html  
  
# Configure moodle  
COPY ./config-moodle.php /var/www/html/config.php  
  
# Setup moodle env  
RUN mkdir /var/moodledata  
RUN chown www-data:www-data /var/moodledata  
  
# Foreground  
ADD ./foreground.sh /etc/apache2/foreground.sh  
RUN chmod +x /etc/apache2/foreground.sh  
  
VOLUME ["/var/moodledata"]  
  
CMD ["/etc/apache2/foreground.sh"]

