FROM nginx:1.10.1  
EXPOSE 80  
COPY conf.d /etc/nginx/conf.d/  
CMD mkdir /var/www/html/health  
ADD index.html /var/www/html/health/index.html  
  
ADD start.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/start.sh  
  
CMD ["usr/local/bin/start.sh"]  

