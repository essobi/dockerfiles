FROM wrfly/supervisor-nginx-php:latest  
COPY fc-init.sh top_1000.txt /  
COPY app /app  
RUN chmod +x /fc-init.sh  
CMD ["/fc-init.sh"]  

