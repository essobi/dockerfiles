# Stack Exchange Cross-Tag Analysis nginx web server  
  
# Pull base image  
FROM nginx:1.7  
  
# Remove default configuration files  
RUN rm /etc/nginx/conf.d/default.conf  
RUN rm /etc/nginx/conf.d/example_ssl.conf  
  
# Copy custom configuration file  
COPY secta.conf /etc/nginx/conf.d/secta.conf  

