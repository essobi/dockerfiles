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
FROM fidesio/ubuntu:trusty  
  
# Maintainer  
MAINTAINER Fidesio <docker@fidesio.com>  
  
### PHP  
# Install PHP  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y php5-cli  
  
# Install PHP extensions  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y php5-imagick php5-gd
php5-intl php5-mcrypt php5-apcu php5-curl php5-mysql  
  
# Download & Add Elasticache Cluster Client  
RUN wget http://elasticache-
downloads.s3.amazonaws.com/ClusterClient/PHP-5.5/latest-64bit -O - | tar -C
/opt -xz  
RUN cp /opt/AmazonElastiCacheClusterClient*/amazon-elasticache-cluster-
client.so /usr/lib/php5/20121212/  
RUN cp /opt/AmazonElastiCacheClusterClient*/memcached.ini /etc/php5/mods-
available/  
RUN echo "extension=amazon-elasticache-cluster-client.so" >> /etc/php5/mods-
available/amazon-elasticache-cluster-client.ini  
  
# Enable Elasticache Cluster Client  
RUN php5enmod amazon-elasticache-cluster-client  
RUN php5enmod memcached  
  
### /PHP  
### wkhtmltoxxxx  
# Download and install wkhtmltopdf/wkhtmltoimage  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y xorg libssl-dev
libxrender-dev  
  
# Download and install wkhtmltopdf  
RUN wget
https://wkhtmltopdf.googlecode.com/files/wkhtmltopdf-0.10.0_rc2-static-
amd64.tar.bz2  
RUN tar xvjf wkhtmltopdf-0.10.0_rc2-static-amd64.tar.bz2  
RUN install wkhtmltopdf-amd64 /usr/bin/wkhtmltopdf  
  
# Download and install wkhtmltoimage  
RUN wget
https://wkhtmltopdf.googlecode.com/files/wkhtmltoimage-0.10.0_rc2-static-
amd64.tar.bz2  
RUN tar xvjf wkhtmltoimage-0.10.0_rc2-static-amd64.tar.bz2  
RUN install wkhtmltoimage-amd64 /usr/bin/wkhtmltoimage  
  
### /wkhtmltoxxxx  

