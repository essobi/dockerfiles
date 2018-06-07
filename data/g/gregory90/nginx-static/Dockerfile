FROM gregory90/nginx:1.7.9  
  
ADD nginx/default /etc/nginx/sites-available/default  
ADD nginx/default /etc/nginx/sites-enabled/default  
ADD run.sh /app/run.sh  
RUN chmod +x /app/run.sh  
  
CMD ["/app/run.sh"]  

