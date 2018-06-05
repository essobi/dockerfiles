FROM gliderlabs/consul  
MAINTAINER WOW! Group Development  
  
ADD ./runner /runner  
ADD ./config /config/  
EXPOSE 53 53/udp 8300 8301 8301/udp 8302 8302/udp 8400 8500  
  
ENTRYPOINT ["/runner"]  

