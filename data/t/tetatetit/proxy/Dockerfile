FROM jwilder/nginx-proxy  
  
RUN echo "\  
client_max_body_size 20m;\n\  
proxy_connect_timeout 700;\n\  
proxy_send_timeout 900;\n\  
proxy_read_timeout 900;\n\  
" > /etc/nginx/conf.d/webapps.conf  

