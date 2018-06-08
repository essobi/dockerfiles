FROM jwilder/nginx-proxy:latest  
  
RUN touch /etc/nginx/conf.d/my_proxy.conf  
  
RUN { \  
echo 'proxy_set_header X-Forwarded-Host $host;'; \  
echo 'proxy_set_header X-Forwarded-Port $server_port;'; \  
echo 'client_max_body_size 256m;'; \  
echo 'proxy_redirect off;'; \  
} > /etc/nginx/conf.d/my_proxy.conf  

