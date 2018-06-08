FROM alpine:3.7  
LABEL maintainer Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
COPY run-quasselcore.sh /usr/bin/run-quasselcore.sh  
  
RUN apk --update add git quassel-core qt-postgresql  
  
USER quassel  
EXPOSE 4242/tcp  
VOLUME ["/secret", "/var/log/quassel", "/var/lib/quassel"]  
ENTRYPOINT ["/bin/sh", "/usr/bin/run-quasselcore.sh"]  

