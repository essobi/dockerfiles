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
  
### nodejs  
# install npm  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
### /nodejs  
### handlebars  
# install handlebars  
RUN npm install --global handlebars@2.0.0-alpha.4  
  
### /handlebars  
RUN rm -fr /etc/apache2/sites-enabled/0-virtual-host.conf  
  
ADD ./virtual-host.conf /etc/apache2/sites-enabled/0-virtual-host.conf  
  
RUN mkdir -p /var/www/web  
  
ADD index.php /var/www/web/index.php  

