FROM phusion/baseimage:0.9.16  
MAINTAINER Pavel Mironov <wanderermg@gmail.com>  
  
CMD ["/sbin/my_init"]  
  
ADD tor.list /etc/apt/sources.list.d/tor.list  
RUN apt-get update -y && \  
apt-get dist-upgrade -y && \  
apt-get install deb.torproject.org-keyring -y --force-yes && \  
apt-get update -y && \  
apt-get install tor -y && \  
echo "SocksPort 0.0.0.0:9050" >> /etc/tor/torrc && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD tor.sh /etc/service/tor/run  
  
EXPOSE 9050  

