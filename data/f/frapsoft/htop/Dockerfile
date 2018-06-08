FROM alpine  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
RUN \  
adduser -h /app -s /bin/nologin -D app && \  
apk add --update --no-cache htop && \  
rm -f /tmp/* /etc/apk/cache/*  
  
USER app  
  
WORKDIR /app  
  
ENTRYPOINT ["htop"]  

