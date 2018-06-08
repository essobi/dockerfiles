# patrickhoefler.net nginx web server  
# Pull base image  
FROM nginx:1.7  
# Remove default ssl configuration file  
RUN rm /etc/nginx/conf.d/example_ssl.conf  
  
# Copy web content  
RUN rm /usr/share/nginx/html/*  
COPY www /usr/share/nginx/html  

