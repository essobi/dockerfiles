FROM resin/raspberry-pi-alpine:3.6  
RUN [ "cross-build-start" ]  
  
MAINTAINER Matthew Schick <matthew.schick@gmail.com>  
  
RUN apk --no-cache add nginx \  
nginx-mod-stream && \  
mkdir -p /run/nginx  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN [ "cross-build-end" ]  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]  

