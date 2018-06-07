FROM ubuntu:15.04  
MAINTAINER "The Impact Bot" <technology@bcorporation.net>  
  
RUN apt-get update && \  
apt-get install -y libevent-dev libsasl2-2 sasl2-bin libsasl2-2 libsasl2-dev
libsasl2-modules && \  
apt-get install -y memcached pwgen && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD user.sh /user.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
  
EXPOSE 11211  
CMD ["/run.sh"]  

