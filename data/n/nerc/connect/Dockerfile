FROM nginx  
  
LABEL maintainer "gareth.lloyd@stfc.ac.uk"  
  
COPY content /usr/share/nginx/html  
  
COPY ./docker-entrypoint.sh /  
  
CMD ["/docker-entrypoint.sh"]

