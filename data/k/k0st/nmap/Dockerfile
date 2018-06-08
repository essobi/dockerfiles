FROM gliderlabs/alpine  
MAINTAINER Vlatko Kosturjak kost@kost.im  
  
RUN apk --update add nmap && rm -f /var/cache/apk/*  
  
RUN mkdir /work  
VOLUME ["/work"]  
WORKDIR /work  
  
ENTRYPOINT ["nmap"]  
  

