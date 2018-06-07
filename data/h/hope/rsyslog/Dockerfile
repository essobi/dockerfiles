FROM hope/base-alpine:3.4  
MAINTAINER Sergey Sadovoi <sergey@hope.ua>  
  
ENV \  
RSYSLOG_VERSION=8.18.0  
COPY container-files/ /tmp/  
  
RUN \  
# Install and configure  
apk add \--no-cache rsyslog && \  
cp -rf /tmp/etc / && \  
  
# Entrypoint  
cp -f /tmp/*.sh / && \  
chmod +x /run.sh && \  
  
# Cleanup  
rm -rf "/tmp/"*  
  
EXPOSE 514  
ENTRYPOINT ["/run.sh"]  

