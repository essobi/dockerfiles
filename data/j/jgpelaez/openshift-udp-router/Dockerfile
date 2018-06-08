FROM alpine:3.4  
MAINTAINER Juan Carlos García Peláez <juancarlosgpelaez@gmail.com>  
  
ADD docker-entrypoint.sh /usr/local/bin/  
RUN apk add --no-cache socat libcap && \  
chmod 755 /usr/local/bin/docker-entrypoint.sh && \  
setcap 'cap_net_bind_service=ep' /usr/bin/socat && \  
rm -rf /var/cache/apk/*  
  
USER 1001  
ENTRYPOINT /usr/local/bin/docker-entrypoint.sh  

