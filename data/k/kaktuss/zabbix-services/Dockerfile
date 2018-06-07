FROM alpine:3.5  
RUN \  
apk add --no-cache \  
perl \  
perl-json \  
perl-libwww \  
zabbix-utils  
  
ENV CONSUL_HTTP_ADDR=consul.service.consul:8500  
ENV CONSUL_TOKEN=  
  
ENV SRV_DISCOVERY_KEY=services_discovery  
ENV SRV_ITEM_KEY=service_item  
ENV SRV_HOSTNAME=  
ENV SRV_ZABBIX_SERVER=  
  
ENV SRV_CHECK_PERIOD=15  
COPY services.pl /usr/local/bin/services.pl  
COPY start.sh /usr/local/bin/start.sh  
  
CMD ["/usr/local/bin/start.sh"]  

