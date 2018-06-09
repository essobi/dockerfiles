FROM alpine:latest  
  
MAINTAINER tabsun <buptmsg@gmail.com>  
  
RUN apk --update add nginx  
  
RUN sed -i "s#root html;#root /usr/share/nginx/html;#g" /etc/nginx/nginx.conf  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log  
  
COPY . /usr/share/nginx/html  
  
EXPOSE 80  
CMD ["nginx", "-g", "pid /tmp/nginx.pid; daemon off;"]

