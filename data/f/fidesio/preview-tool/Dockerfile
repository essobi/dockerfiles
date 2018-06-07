# Dockerfile for preview  
#  
# Details:  
# - Ubuntu 14.04 x64  
# - PHP5.5  
# - wkhtmltopdf 0.10.0 rc2  
# - wkhtmltoimage 0.10.0 rc2  
# - Bower  
##  
# Pull base image.  
FROM fidesio/preview-base:trusty  
  
# Maintainer  
MAINTAINER Fidesio <docker@fidesio.com>  
# Install Subversion  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y subversion  
  
# Create /var/www  
RUN mkdir -p /var/www  
  
### nodejs  
# install npm  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
### /nodejs  
### bower  
# install bower  
RUN npm install \--global bower  
  
### /bower  
### handlebars  
# install handlebars  
RUN npm install \--global handlebars@2.0.0-alpha.4  
  
### /handlebars  
ADD ./update-code.sh /tmp/update-code.sh  
ADD ./update-code-www-data.sh /tmp/update-code-www-data.sh  
  
ADD ./create-db.sh /tmp/create-db.sh  
ADD ./create-db-www-data.sh /tmp/create-db-www-data.sh  
ADD ./update-db.sh /tmp/update-db.sh  
ADD ./update-db-www-data.sh /tmp/update-db-www-data.sh

