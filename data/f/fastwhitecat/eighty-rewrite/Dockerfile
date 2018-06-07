FROM nginx:1.10.1  
COPY conf.d /etc/nginx/conf.d/  
COPY index.html /var/www/html/index.html  
  
EXPOSE 80  
ADD start.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/start.sh  
  
CMD ["usr/local/bin/start.sh"]

