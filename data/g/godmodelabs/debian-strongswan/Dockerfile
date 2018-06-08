FROM debian:latest  
MAINTAINER it-operations@boerse-go.de  
  
RUN apt-get update -y && \  
apt-get install -y iptables strongswan kmod vim  
  
EXPOSE 500/udp 4500/udp  
  
CMD /usr/sbin/ipsec start --nofork  

