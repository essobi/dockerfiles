FROM alpine  
  
EXPOSE 8080  
ENV SERVICE_NAME ""  
ENV CONSUL_ADDR ""  
RUN apk update && apk add haproxy && rm -rf /var/cache/apk/*  
  
ADD consul-template_0.18.1_linux_amd64.tgz /usr/sbin  
ADD haproxy.cfg.ctmpl.sed /  
ADD entrypoint.sh /  
  
CMD ["/entrypoint.sh"]  

