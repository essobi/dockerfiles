FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && apt-get install -y vpnc iptables net-tools iputils-
ping iputils-tracepath  
  
# Clean up  
RUN apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Copy run script  
RUN mkdir -p /etc/service/vpnc  
COPY bin/vpnc.sh /etc/service/vpnc/run  
CMD ["/etc/service/vpnc/run"]  

