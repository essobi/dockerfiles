FROM alpine:3.5  
MAINTAINER Fabien Schurter <fabien@fabschurt.com>  
  
RUN apk update --no-cache && \  
apk add nginx && \  
mkdir /run/nginx && \  
rm -rf /etc/nginx/conf.d/* \  
/var/cache/apk/*  
COPY config/nginx.conf /etc/nginx  
ONBUILD COPY config/nginx/*.conf /etc/nginx/conf.d/  
  
EXPOSE 80  
CMD ["nginx"]  

