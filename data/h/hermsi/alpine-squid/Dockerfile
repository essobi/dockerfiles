FROM alpine:latest  
  
LABEL maintainer="https://github.com/Hermsi1337"  
  
ENV SQUID_CONFIG_PATH=/etc/squid/squid.conf \  
SQUID_DEBUG_LEVEL=2  
RUN apk update && \  
apk upgrade && \  
apk add squid && \  
rm -rf /tmp/* /var/cache/apk/*  
  
COPY start.sh /usr/local/bin/startsquid  
  
CMD ["/usr/local/bin/startsquid"]

