FROM alpine  
  
RUN apk update && \  
apk add aria2 nginx && \  
mkdir -p /var/run/nginx  
  
ADD ./nginx.conf /etc/nginx/nginx.conf  
ADD ./aria2.conf /aria2.conf  
ADD ./webui-aria2 /var/www/aria2  
  
EXPOSE 80 6800  
CMD ["sh", "-c", "nginx && aria2c --conf-path=/aria2.conf"]  

