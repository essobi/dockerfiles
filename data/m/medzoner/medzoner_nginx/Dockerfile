FROM nginx:1.11  
RUN rm -rf /var/www  
RUN mkdir -p /var/www  
  
RUN usermod -u 1000 www-data  
RUN chown -R www-data:www-data /var/www  
  
CMD ["nginx", "-g", "daemon off;"]  

