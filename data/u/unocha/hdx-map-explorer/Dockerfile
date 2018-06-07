FROM alpine:3.5  
MAINTAINER "Serban Teodorescu <teodorescu.serban@gmail.com>"  
COPY ./bin /var/www/  
  
COPY env/etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf  
  
RUN apk add --update-cache \  
nginx && \  
mkdir -p /run/nginx && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["nginx", "-g", "daemon off;"]  

