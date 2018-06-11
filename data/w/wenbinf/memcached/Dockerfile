############################################################  
# Dockerfile to build memcached images  
############################################################  
  
FROM wenbinf/base  
ADD run /root/  
RUN chmod 755 /root/run  
  
MAINTAINER Wenbin Fang <wenbin@cs.wisc.edu>  
  
# Install and configure memcached.  
RUN apt-get -qq update && \  
apt-get -qq install memcached && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN sed -i -e 's/^-l 127.0.0.1/-l 0.0.0.0/' /etc/memcached.conf  
RUN sed -i -e 's/-u memcache/-u root/' /etc/memcached.conf  
RUN rm -f /etc/init.d/memcached  
  
EXPOSE 11211  

