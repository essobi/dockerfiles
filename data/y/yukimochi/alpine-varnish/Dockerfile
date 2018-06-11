FROM alpine:edge  
  
RUN apk -U upgrade && \  
apk add varnish && \  
rm -rf /tmp/* /var/cache/apk/*  
  
WORKDIR /etc/varnish  
  
VOLUME [ "/etc/varnish" ]  
EXPOSE 80  
CMD [ "/usr/sbin/varnishd", "-F", "-f", "/etc/varnish/default.vcl", "-s",
"malloc,1G", "-a", "0.0.0.0:80" ]  

