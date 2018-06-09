FROM debian:wheezy  
  
MAINTAINER Tommy Lau <tommy@gen-new.com>  
  
# Install the needed packages for OpenWrt  
RUN apt-get update && apt-get install -y dnsmasq --no-install-recommends && rm
-rf /var/lib/apt/lists/*  
  
EXPOSE 53  
  
CMD ["/usr/sbin/dnsmasq", "-d"]  
  

