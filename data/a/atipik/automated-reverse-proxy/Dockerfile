FROM jwilder/nginx-proxy  
  
RUN sed -i "s/http {/http {\n client_max_body_size 50M;/"
/etc/nginx/nginx.conf  
RUN sed -i "s/http {/http {\n proxy_connect_timeout 600;/"
/etc/nginx/nginx.conf  
RUN sed -i "s/http {/http {\n proxy_send_timeout 600;/" /etc/nginx/nginx.conf  
RUN sed -i "s/http {/http {\n proxy_read_timeout 600;/" /etc/nginx/nginx.conf  
RUN sed -i "s/http {/http {\n send_timeout 600;/" /etc/nginx/nginx.conf  

