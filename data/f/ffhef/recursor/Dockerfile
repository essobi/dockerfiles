FROM ffhef/debian-batman:8.3-2017.0  
  
MAINTAINER Nico - Freifunk Hennef <nico@freifunk-hennef.de>  
  
RUN apt-get update && apt-get install -y pdns-recursor && apt-get clean && \  
rm -rf /var/lib/apt/lists /tmp/* /var/tmp/*  
  
EXPOSE 53/tcp  
EXPOSE 53/udp  
  
ENTRYPOINT ["/usr/sbin/pdns_recursor"]

