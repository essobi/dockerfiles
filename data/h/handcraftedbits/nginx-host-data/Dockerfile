FROM alpine:3.5  
MAINTAINER HandcraftedBits <opensource@handcraftedbits.com>  
  
COPY data /  
  
VOLUME /etc/letsencrypt  
VOLUME /etc/nginx/host/units  
VOLUME /var/www  
  
RUN apk update && \  
apk add bash  
  
CMD ["/bin/sh", "/opt/container/script/run-data.sh"]  

