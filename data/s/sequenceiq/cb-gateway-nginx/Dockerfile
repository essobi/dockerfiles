FROM nginx:1.9  
MAINTAINER SequenceIQ  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD 50x.json /usr/share/nginx/json/50x.json  
  
COPY ./docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

