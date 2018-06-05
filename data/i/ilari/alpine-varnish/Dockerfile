FROM alpine:3.3  
MAINTAINER ilari.makela@wunderkraut.com  
  
ADD start.sh /start.sh  
# Update the package repository and install applications  
RUN apk --no-cache --update add varnish && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/* && \  
chmod 755 /start.sh  
  
# Make our default VCL available on the container  
ADD default.vcl /etc/varnish/default.vcl  
  
ENV VARNISH_BACKEND_PORT 80  
ENV VARNISH_BACKEND_HOST 192.168.1.1  
ENV VARNISH_PORT 80  
ENV VARNISH_MEMORY 100M  
  
# Expose port 80  
EXPOSE 80  
CMD ["/start.sh"]

