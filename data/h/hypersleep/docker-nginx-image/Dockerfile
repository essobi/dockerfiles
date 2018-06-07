FROM nginx  
  
COPY nginx.conf /etc/nginx/nginx.conf  
RUN mkdir -p /etc/nginx/conf.d  
COPY conf.d/*.conf /etc/nginx/conf.d/  

