# Dockerfile for sniproxy on Fedora  
FROM fedora  
  
MAINTAINER jason@ramtechusa.com  
  
RUN yum -y install udns-devel sniproxy  
  
CMD ["/usr/sbin/sniproxy", "-c", "/data/sniproxy.conf", "-f"]  

