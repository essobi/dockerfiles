FROM alpine  
  
EXPOSE 8080  
ENV SERVICE_NAME ""  
ENV CONSUL_ADDR ""  
ENV CACHE_SIZE 100M  
ENV VARNISHD_PARAMS -p default_ttl=3600 -p default_grace=3600  
RUN apk update && apk add varnish && rm -rf /var/cache/apk/*  
  
ADD consul-template_0.18.1_linux_amd64.tgz /usr/sbin  
ADD default.vcl.ctmpl.sed /  
ADD entrypoint.sh /  
  
CMD ["/entrypoint.sh"]  

