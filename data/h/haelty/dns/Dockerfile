FROM alpine:3.4  
MAINTAINER dusartnicolas@gmail.com  
  
RUN apk update && apk upgrade  
RUN apk add dnsmasq  
  
COPY dnsmasq.conf /etc/dnsmasq.conf  
  
VOLUME ["/config"]  
  
EXPOSE 53  
ENTRYPOINT ["dnsmasq", "-k"]  

