FROM nginx:1.12-alpine  
  
RUN rm /etc/nginx/conf.d/default.conf  
  
ENV STATIC_PATH=  
  
COPY static.conf.template /etc/nginx/conf.d/static.conf.template  
COPY start.sh /usr/local/bin/start.sh  
  
CMD ["/usr/local/bin/start.sh"]  

