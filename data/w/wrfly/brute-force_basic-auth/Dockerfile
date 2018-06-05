FROM nginx:latest  
COPY default.conf /etc/nginx/conf.d/default.conf  
COPY top_1000.txt fc-init.sh /  
RUN chmod +x /fc-init.sh  
CMD ["/fc-init.sh"]  

