# Dockerfile for sniproxy on Fedora  
FROM fedora  
  
MAINTAINER anton@belodedenko.me  
  
RUN dnf -y install findutils iproute net-tools udns-devel sniproxy sipcalc  
  
ADD functions /opt/functions  
  
ADD sniproxy.sh /opt/sniproxy.sh  
ADD sniproxy.conf /data/conf/sniproxy.conf  
  
CMD /opt/sniproxy.sh  

