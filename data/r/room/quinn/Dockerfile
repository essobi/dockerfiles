FROM tutum/nginx:latest  
  
#RUN rm /etc/nginx/conf.d/default.conf  
#COPY sites-enabled/static_site /etc/nginx/conf.d/default.conf  
RUN rm /etc/nginx/sites-enabled/default  
ADD sites-enabled/ /etc/nginx/sites-enabled  
  
EXPOSE 80  

