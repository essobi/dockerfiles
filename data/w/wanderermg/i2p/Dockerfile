FROM phusion/baseimage:0.9.16  
MAINTAINER Pavel Mironov <wanderermg@gmail.com>  
  
CMD ["/sbin/my_init"]  
  
RUN apt-add-repository ppa:i2p-maintainers/i2p -y && \  
apt-get update -y && \  
apt-get dist-upgrade -y && \  
apt-get install i2p -y  
  
ADD i2p.sh /etc/service/i2p/run  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
EXPOSE 4444 4445 7657  

