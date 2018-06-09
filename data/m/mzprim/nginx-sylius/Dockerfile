FROM nginx  
  
RUN usermod -u 1000 www-data  
ADD nginx.conf /etc/nginx/  
COPY sites-enabled/sylius.conf /etc/nginx/conf.d/  
  
CMD ["nginx"]  
  
EXPOSE 80  
EXPOSE 443  

