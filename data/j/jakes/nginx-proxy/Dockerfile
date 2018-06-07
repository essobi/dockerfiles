FROM jwilder/nginx-proxy  
MAINTAINER Jakes Lee <jakeslee66@gmail.com>  
  
#Turn on spdy for ssl  
RUN sed -i 's/443 ssl;/443 ssl spdy;/g' /app/nginx.tmpl  
  
#Turn off echo nginx's version while errors occurred.  
RUN echo 'server_tokens off;' > /etc/nginx/conf.d/my_proxy.conf  

