FROM nginx  
COPY api.conf /etc/nginx/sites-enabled/api.conf  
COPY web.conf /etc/nginx/sites-enabled/web.conf  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY run.sh /etc/nginx/run.sh  
CMD ["/etc/nginx/run.sh"]  

