FROM alpine:3.4  
MAINTAINER nownabe  
  
RUN apk add --no-cache --update dnsmasq \  
&& mkdir /etc/dnsmasq.d  
COPY dnsmasq.conf /etc/dnsmasq.conf  
  
EXPOSE 53 53/udp  
CMD /usr/sbin/dnsmasq --keep-in-foreground  

