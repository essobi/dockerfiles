FROM jwilder/nginx-proxy  
  
MAINTAINER Ian Lintner "ian.lintner@workiva.com"  
RUN { \  
echo 'server_tokens off;'; \  
echo 'client_max_body_size 500m;'; \  
} > /etc/nginx/conf.d/my_proxy.conf  

