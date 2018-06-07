# Based on a light and trusted image  
FROM debian:jessie  
  
MAINTAINER Herve Nicol  
  
ENV DEBIAN_FRONTEND=noninteractive  
# Update packages list  
RUN apt-get update && apt-get install -y unzip  
  
ADD https://github.com/ldleman/Leed/archive/master.zip /tmp/leed.zip  
RUN mkdir -p /var/www \  
&& cd /tmp \  
&& unzip leed.zip \  
&& mv Leed-master /var/www/html  
ADD https://github.com/ldleman/Leed-market/archive/master.zip /tmp/leed-
market.zip  
RUN cd /tmp \  
&& unzip leed-market.zip \  
&& mv Leed-market-master/* /var/www/html/plugins/  
  
#Config file  
#ADD conf/constant.php /var/www/html/  
LABEL description="Jessie / Apache 2.4 / Leed"  
  
VOLUME /var/www/html  
  

