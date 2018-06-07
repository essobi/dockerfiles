# Dockerfile for preview  
#  
# Details:  
# - Ubuntu 14.04 x64  
# - PHP5.5  
# - wkhtmltopdf 0.11.0 rc1  
# - wkhtmltoimage 0.11.0 rc1  
##  
# Pull base image.  
FROM fidesio/preview-base:trusty  
  
# Maintainer  
MAINTAINER Fidesio <docker@fidesio.com>  
  
### Supervisor  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y supervisor  
  
RUN mkdir -p /var/log/supervisor  
  
ADD supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
### SSHD  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-server  
  
RUN echo 'root:root' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
RUN mkdir -p /var/run/sshd  
  
ADD supervisor/sshd.conf /etc/supervisor/conf.d/sshd.conf  
  
EXPOSE 22  
### Apache2  
# Install Apache2  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apache2 libapache2-mod-
php5  
  
RUN a2enmod rewrite  
  
# Create logs directory  
RUN mkdir -p /var/lock/apache2 /var/run/apache2  
  
# Remove default virtual host  
RUN rm -rf /etc/apache2/sites-enabled/000-default.conf  
  
# Add our virtual-host.conf  
ADD ./virtual-host.conf /etc/apache2/sites-enabled/0-virtual-host.conf  
  
# Override PHP Configuration  
ADD ./99-php.ini /etc/php5/apache2/conf.d/99-php.ini  
  
RUN mkdir -p /tmp/apache2  
RUN chown www-data:www-data /tmp/apache2  
  
### /Apache2  
### PHP directories  
RUN mkdir -p /tmp/php-session  
RUN mkdir -p /tmp/php-apc  
RUN mkdir -p /tmp/php-upload-tmp  
RUN mkdir -p /tmp/php-wsdl-cache  
  
RUN chown www-data:www-data /tmp/php-*  
  
### /PHP directories  
ADD supervisor/apache2.conf /etc/supervisor/conf.d/apache2.conf  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]

