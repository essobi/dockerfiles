FROM phusion/baseimage:0.9.17  
MAINTAINER caraka  
  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# upgrade the OS and install privoxy openvpn  
RUN export DEBIAN_FRONTEND='noninteractive' &&\  
apt-get update && apt-get upgrade -y -o Dpkg::Options::="--force-confold" &&\  
apt-get install -y --no-install-recommends iptables openvpn privoxy nano wget
&&\  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# privoxy & openvpn config  
ADD privoxy /etc/privoxy/  
ADD pia /etc/openvpn/  
  
# scripts  
RUN mkdir /etc/service/privoxy  
ADD /scripts/privoxy.sh /etc/service/privoxy/run  
  
RUN mkdir /etc/service/openvpn  
ADD /scripts/openvpn.sh /etc/service/openvpn/run  
  
RUN mkdir -p /etc/my_init.d  
ADD /scripts/start.sh /etc/my_init.d/start.sh  
  

