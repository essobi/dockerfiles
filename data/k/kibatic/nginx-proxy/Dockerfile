FROM jwilder/nginx-proxy  
  
RUN { \  
echo 'server_tokens off;'; \  
echo 'client_max_body_size 100m;'; \  
echo 'proxy_read_timeout 180s;'; \  
echo 'proxy_send_timeout 180s;'; \  
} > /etc/nginx/conf.d/my_proxy.conf  

