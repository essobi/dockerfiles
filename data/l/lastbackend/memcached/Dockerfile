FROM ubuntu:trusty  
  
MAINTAINER team@lastbackend.com  
  
# Install memcached  
RUN apt-get update && \  
apt-get install -y libevent-dev libsasl2-2 sasl2-bin libsasl2-2 libsasl2-dev
libsasl2-modules && \  
apt-get install -y memcached pwgen && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
# Add scripts  
ADD init.sh /init.sh  
RUN chmod +x /*.sh  
  
EXPOSE 11211  
CMD ["/init.sh"]

