FROM vmwarecna/nginx  
ADD server.conf /etc/nginx/conf.d/server.conf  
  
RUN mkdir -p /var/www/html  
ADD index.html /var/www/html/index.html  
  
ADD nginx.conf /etc/nginx/nginx.conf  
RUN cp /usr/share/nginx/html/splash.jpg /var/www/html/splash.jpg  

