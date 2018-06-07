FROM nginx  
  
RUN rm /etc/nginx/conf.d/default.conf  
RUN mkdir /etc/nginx/ssl  
  
COPY sites /usr/share/nginx/html  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY conf.d /etc/nginx/conf.d  
  
VOLUME /etc/nginx/ssl  
VOLUME /var/log/nginx/log  

