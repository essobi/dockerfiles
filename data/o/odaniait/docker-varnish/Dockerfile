FROM alpine:3.5  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
# Set correct environment variables.  
ENV HOME /root  
  
RUN apk update && \  
apk upgrade && \  
apk --update add curl wget bash htop vim msmtp bind-tools varnish && \  
# Clean APK cache  
rm -rf /var/cache/apk/*  
  
ENV VCL_CONFIG /etc/varnish/default.vcl  
ENV CACHE_SIZE 128m  
ENV LISTEN_PORT 80  
# setup varnish service  
COPY scripts/varnish.sh /opt/varnish.sh  
COPY default.vcl /etc/varnish/default.vcl  
  
VOLUME ["/opt/varnish"]  
CMD '/opt/varnish.sh'  
EXPOSE 80  

