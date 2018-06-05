FROM nginx  
MAINTAINER Oleg Morozenkov  
  
COPY nginx-run.sh /nginx-run.sh  
COPY nginx.conf /etc/nginx/nginx.conf  
RUN rm -rf /etc/nginx/sites-enabled && mkdir -p /etc/nginx/sites-enabled  
  
CMD ["bash", "/nginx-run.sh"]  

