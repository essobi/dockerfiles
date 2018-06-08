# Docker file for rancher-firewall  
FROM alpine  
MAINTAINER Ishi Ruy <dev@nhz.io>  
  
RUN apk add -U iproute2  
  
ENV IF eth0  
ENV TCP_PORTS 22,80,443  
ENV UDP_PORTS 500,4500  
  
CMD iptables -t mangle -F \  
&& iptables -t mangle -A PREROUTING -i $IF -m conntrack --ctstate NEW -m
multiport -p tcp \\! --dports $TCP_PORTS -j DROP \  
&& iptables -t mangle -A PREROUTING -i $IF -m conntrack --ctstate NEW -m
multiport -p udp \\! --dports $UDP_PORTS -j DROP \  
&& while true; do sleep 86400; done  

