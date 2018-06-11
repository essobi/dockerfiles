FROM alpine  
MAINTAINER Walker Lee <walkerlee.tw@gmail.com>  
  
RUN apk -U --no-cache add nginx \  
&& sed -i '/http {/a autoindex on;' /etc/nginx/nginx.conf \  
&& ln -s /dev/stdout /var/log/nginx/access.log \  
&& ln -s /dev/stderr /var/log/nginx/error.log \  
&& mkdir -p /run/nginx \  
&& rm -rf /var/cache/apk/*  
  
COPY default.conf /etc/nginx/conf.d/default.conf  
  
VOLUME ["/var/lib/nginx/html"]  
EXPOSE 80  
CMD ["nginx", "-g", "daemon off;"]  

