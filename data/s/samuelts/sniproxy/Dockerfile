#  
# Dockerfile for sniproxy  
#  
FROM alpine:latest  
MAINTAINER Samuel X.S. Tseng <samuel.zxs@gmail.com>  
  
# install sniproxy & dnsmasq.  
ENV PKGS sniproxy dnsmasq  
RUN apk --update add --no-cache $PKGS  
  
COPY docker-entrypoint.sh /  
COPY sniproxy.conf /etc/sniproxy/sniproxy.conf  
RUN chmod +x /docker-entrypoint.sh  
  
EXPOSE 80 443  
ENTRYPOINT ["/docker-entrypoint.sh"]  

