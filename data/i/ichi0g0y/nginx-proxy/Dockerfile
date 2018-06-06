FROM jwilder/nginx-proxy  
MAINTAINER yl0g0ly <yl0g0ly [at] gmail.com>  
  
RUN { \  
echo 'client_max_body_size 10G;'; \  
echo 'client_body_buffer_size 128K;'; \  
} > /etc/nginx/conf.d/my_proxy.conf  

