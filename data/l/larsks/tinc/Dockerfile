FROM alpine  
  
EXPOSE 655/udp  
VOLUME /etc/tinc  
ENTRYPOINT ["tincd", "-D"]  
  
RUN apk update  
RUN apk add tinc tcpdump iptables dnsmasq  

