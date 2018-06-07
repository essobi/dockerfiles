FROM janeczku/debian-nginx:latest  
MAINTAINER Jan Broer <janeczku@yahoo.com>  
  
RUN \  
apt-wrap apt-get update && \  
  
# Add newrelic repository  
wget -qO - http://download.newrelic.com/548C16BF.gpg | apt-key add \- && \  
sh -c 'echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list' &&\  
  
# Add dotdeb php56 repository  
sh -c 'echo "deb http://packages.dotdeb.org wheezy-php56 all" >>
/etc/apt/sources.list.d/doteb.list' && \  
sh -c 'echo "deb-src http://packages.dotdeb.org wheezy-php56 all" >>
/etc/apt/sources.list.d/doteb.list' && \  
apt-wrap apt-get update && \  
  
# Install PHP 5.6 and modules php5-zendopcache  
apt-wrap apt-get install -y php5-fpm php5-cli php5-gd php5-intl php5-curl
php5-mysql php5-redis php5-mcrypt php5-common newrelic-php5 && \  
  
# Clean up  
apt-clean  
  
COPY rootfs /  

