FROM petitchevalroux/php-fpm  
MAINTAINER Patrick Poulain <docker@m41l.me>  
  
# install pluxml and dependencies  
RUN apt-get update && \  
apt-get -y install git php5-gd && \  
rm -rf /var/www/* && \  
git clone https://github.com/pluxml/PluXml.git /var/www  
  
# cleaning to reduce image size  
RUN apt-get -y purge git && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# setting right  
# user-id 1000 is the one owning volume so www-data can write in  
RUN find /var/www -type d -exec chmod o=rx {} \; && \  
find /var/www -type f -exec chmod o=r {} \; && \  
usermod -u 1000 www-data && \  
chown -R root:root /var/www && \  
chown -R www-data:www-data /var/www/data

