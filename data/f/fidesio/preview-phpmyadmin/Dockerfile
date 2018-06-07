# Dockerfile for preview  
#  
# Details:  
# - Ubuntu 14.04 x64  
# - PHP5.5  
# - wkhtmltopdf 0.11.0 rc1  
# - wkhtmltoimage 0.11.0 rc1  
##  
# Pull base image.  
FROM fidesio/preview-apache2:trusty  
  
# Maintainer  
MAINTAINER Fidesio <docker@fidesio.com>  
  
### Apache2  
# Install Apache2  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y phpmyadmin  
  
RUN rm -fr /etc/apache2/sites-enabled/0-virtual-host.conf  
ADD ./virtual-host.conf /etc/apache2/sites-enabled/0-virtual-host.conf  
  
RUN rm -fr /etc/phpmyadmin/config-db.php  
ADD ./config-db.php /etc/phpmyadmin/config-db.php

