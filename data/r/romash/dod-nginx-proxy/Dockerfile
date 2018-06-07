FROM nginx:stable-alpine  
MAINTAINER Romash <tcp6000@gmail.com>  
  
# Copy configs  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY map_block_http_methods.conf /etc/nginx/map_block_http_methods.conf  
COPY nginx_status_allowed_hosts.conf
/etc/nginx/nginx_status_allowed_hosts.conf  
COPY blacklist.conf /etc/nginx/blacklist.conf  
COPY reverse_proxy.conf /etc/nginx/reverse_proxy.conf  
  
CMD ["nginx", "-g", "daemon off;"]  

