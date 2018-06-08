FROM alpine:edge  
MAINTAINER Lyndon Li <snakeliwei@gmail.com>  
  
RUN apk add \--update \--no-cache nginx tzdata \  
&& cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& apk del tzdata \  
&& mkdir -p /etc/nginx/sites-enabled \  
&& mkdir -p /ssl \  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY nginx.conf /etc/nginx/nginx.conf  
  
EXPOSE 80 443  
STOPSIGNAL SIGTERM  
  
CMD ["nginx", "-g", "daemon off;"]  

