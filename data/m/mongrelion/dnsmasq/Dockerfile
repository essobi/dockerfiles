FROM gliderlabs/alpine  
  
MAINTAINER Carlos León <mail@carlosleon.info>  
  
RUN apk-install dnsmasq  
  
ONBUILD COPY ./dnsmasq.conf /etc/dnsmasq.conf  
  
ENTRYPOINT ["/usr/sbin/dnsmasq"]  
  
CMD ["-d", "-q", "-k", "--user=root"]  

