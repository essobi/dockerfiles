FROM jwilder/nginx-proxy  
ENV MAX_BODY_SIZE=50m  
ENV TIMEOUT=60  
CMD { \  
echo "server_tokens off;"; \  
echo "client_max_body_size ${MAX_BODY_SIZE};"; \  
echo "proxy_connect_timeout ${TIMEOUT};"; \  
echo "proxy_send_timeout ${TIMEOUT};"; \  
echo "proxy_read_timeout ${TIMEOUT};"; \  
echo "send_timeout ${TIMEOUT};"; \  
} > /etc/nginx/conf.d/my_proxy.conf && forego start -r  

