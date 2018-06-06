FROM nginx:alpine  
  
RUN echo "set_real_ip_from 10.42.0.0/16; real_ip_header X-Forwarded-For;
real_ip_recursive on;" > /etc/nginx/conf.d/nginx-for-rancher.conf  
  

