# nginx  
#  
# Version 1.0.0  
FROM alpine:3.4  
MAINTAINER Thomas Ingvarsson <ingvarsson.thomas@gmail.com>  
  
RUN apk add --no-cache nginx  
  
# forward request and error logs to docker log collector  
RUN \  
ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80 443  
CMD ["nginx", "-g", "daemon off;"]

