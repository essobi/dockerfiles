FROM ubuntu:14.10  
MAINTAINER Michael Venezia <mike@cc.com>  
  
# INSTALL HHVM  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449 && \  
add-apt-repository 'deb http://dl.hhvm.com/ubuntu utopic main' && \  
apt-get update && \  
apt-get install -y hhvm && \  
apt-get upgrade -y && \  
apt-get remove -y software-properties-common && \  
apt-get autoremove -y  
  
# What ports should we expose - 9001 is the admin port  
EXPOSE 9000 9001  
# Let's modify the php.ini per whatever is in our folder  
ADD php.ini /etc/hhvm/php.ini  
  
# Let's expose the log directory  
VOLUME ["/var/log/hhvm"]  
  
# And this is how we boot the system up  
CMD /usr/bin/hhvm --config /etc/hhvm/php.ini --config /etc/hhvm/server.ini
--user www-data --mode server -vPidFile=/var/run/hhvm/pid  
  

