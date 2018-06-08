FROM alpine:latest  
MAINTAINER Przemek Wesolek <przemek@wesolek.net>  
  
RUN apk add --update socat \  
&& rm -rf /var/cache/apk/*  
  
COPY forward-port.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/forward-port.sh  
  
USER nobody  
  
ENTRYPOINT [ "/usr/local/bin/forward-port.sh"]  

