FROM nginx:alpine  
  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["/start.sh"]  

