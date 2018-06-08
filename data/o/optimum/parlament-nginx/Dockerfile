FROM nginx:alpine  
  
MAINTAINER optimum <info@optimum-web.com>  
  
RUN mkdir -p /tmp/nginx/cache/cache_server_app  
RUN mkdir -p /tmp/nginx/cache/api_cache  
RUN chown -R nginx.nginx /tmp/nginx  
  
ADD site.conf /etc/nginx/conf.d  
RUN rm -f /etc/nginx/nginx.conf  
ADD nginx.conf /etc/nginx/  
RUN rm -f /etc/nginx/conf.d/default.conf  
RUN rm -f /etc/nginx/mime.types  
ADD mime.types /etc/nginx/  
  

