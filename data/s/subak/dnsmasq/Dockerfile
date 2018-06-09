FROM alpine:3.2  
MAINTAINER Subak Systems <info@subak.jp>  
  
RUN apk add -U dnsmasq  
RUN rm -rf /var/cache/apk/*  
  
ONBUILD COPY dnsmasq.conf /etc/  
  
ENTRYPOINT ["dnsmasq", "-d", "-q"]  
CMD ["-h", "-R", "-S", "8.8.8.8", "-S", "129.250.35.250"]  

