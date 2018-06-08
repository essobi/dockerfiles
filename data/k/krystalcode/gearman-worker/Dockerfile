FROM phusion/baseimage  
  
MAINTAINER Dimitris Bozelos <dbozelos@gmail.com>  
  
# Update.  
RUN apt-get update  
  
# Install.  
RUN apt-get install php5-dev php-pear libgearman-dev -y && \  
pecl install gearman  
  
# Clean up.  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Enable gearman extension in php.ini  
# @todo: Set priority in gearman.ini  
RUN cd /etc/php5/cli/conf.d && \  
touch gearman.ini && \  
echo '; configuration for php gearman module' >> gearman.ini && \  
echo '; priority=TBD' >> gearman.ini && \  
echo 'extension=gearman.so' >> gearman.ini  

