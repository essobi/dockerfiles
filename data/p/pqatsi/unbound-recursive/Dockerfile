FROM alpine:latest  
  
MAINTAINER Sonu K. Meena "sonukr666@gmail.com"  
MAINTAINER Leonardo Amaral "git@leonardoamaral.com.br"  
RUN apk add --update unbound curl; \  
rm -rf /var/cache/apk/* ;  
  
COPY unbound.conf /etc/unbound/unbound.conf  
  
RUN mkdir -p /var/unbound/scripts ; mkdir -p /etc/unbound/local.d/  
COPY block_ads_server.sh /var/unbound/scripts/block_ads_server.sh  
COPY docker-entrypoint.sh /var/unbound/scripts/docker-entrypoint.sh  
RUN chmod +x /var/unbound/scripts/*  
RUN chmod a+rw /etc/unbound/  
  
EXPOSE 53/udp 53/tcp  
  
VOLUME /etc/unbound  
  
WORKDIR /var/unbound/scripts  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  

