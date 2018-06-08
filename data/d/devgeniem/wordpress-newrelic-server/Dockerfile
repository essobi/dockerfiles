FROM devgeniem/wordpress-server:debian-php7.0  
MAINTAINER Onni Hakala - Geniem Oy. <onni.hakala@geniem.com>  
  
ARG NR_INSTALL_SILENT=1  
  
# Install newrelic for php  
RUN \  
# Add newrelic as apt-get source  
echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' >
/etc/apt/sources.list.d/newrelic.list \  
&& curl -L https://download.newrelic.com/548C16BF.gpg | apt-key add \- \  
  
# Install package from newrelic  
&& apt-get update \  
&& apt-get install newrelic-php5 -y \  
  
# Cleanup  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /usr/share/doc/*
/var/log/apt/*  
  
# Copy our small changes for newrelic  
COPY rootfs/ /  

