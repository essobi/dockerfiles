FROM ubuntu:14.04  
  
ENV UNBOUND_VERSION=1.5.8  
  
ADD ./install.sh /tmp/install-unbound.sh  
  
RUN apt-get -qq update && \  
apt-get install -y wget && \  
/tmp/install-unbound.sh && \  
rm /tmp/install-unbound.sh && \  
apt-get purge  
  
EXPOSE 53/udp  
  
CMD ["/usr/sbin/unbound", "-d"]  

