FROM jwilder/nginx-proxy  
  
RUN echo 'proxy_buffer_size 128k;' >> /etc/nginx/conf.d/proxy.conf \  
&& echo 'proxy_buffers 4 256k;' >> /etc/nginx/conf.d/proxy.conf \  
&& echo 'proxy_busy_buffers_size 256k;' >> /etc/nginx/conf.d/proxy.conf \  
&& echo 'proxy_connect_timeout 300;' >> /etc/nginx/conf.d/proxy.conf \  
&& echo 'proxy_send_timeout 300;' >> /etc/nginx/conf.d/proxy.conf \  
&& echo 'proxy_read_timeout 300;' >> /etc/nginx/conf.d/proxy.conf \  
&& echo 'send_timeout 300;' >> /etc/nginx/conf.d/proxy.conf  

