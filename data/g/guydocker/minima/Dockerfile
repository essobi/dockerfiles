FROM nginx:alpine  
RUN addgroup -g 1000 -S www-data \  
&& adduser -u 1000 -D -S -G www-data www-data  
  
COPY ./_site /usr/share/nginx/html  

