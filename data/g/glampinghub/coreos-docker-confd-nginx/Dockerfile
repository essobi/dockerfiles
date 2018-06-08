FROM nginx  
MAINTAINER José Luis Salvador Rufo <salvador.joseluis@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY ./confd-0.10.0-linux-amd64 /usr/bin/confd  
COPY ./docker-entrypoint.sh /  
  
RUN chmod +x /usr/bin/confd  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["nginx"]  

