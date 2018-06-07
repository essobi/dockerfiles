FROM alpine  
MAINTAINER add <ohmyadd@gmail.com>  
  
COPY dist /dist  
  
RUN apk add --no-cache hostapd dnsmasq && \  
mv /dist/* /etc/ && \  
rm -rf /var/cache/*  
  
CMD dnsmasq && hostapd /etc/hostapd.conf  

