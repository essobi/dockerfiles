FROM nonameffh/centos:latest  
  
MAINTAINER Aleksey Tarasov <dark.ffh@gmail.com>  
  
ENV FQDN="vpn.example.com"  
ENV container=docker  
  
# install open vpn  
RUN yum -y install openvpn easy-rsa iptables iptables-services initscripts  
  
# add files  
COPY openvpn/ /etc/openvpn/  
COPY bin/* /usr/local/bin/  
RUN chmod a+x /usr/local/bin/*  
  
VOLUME ["/etc/openvpn"]  
EXPOSE 1194/udp  
  
CMD ["ovpn-run"]

