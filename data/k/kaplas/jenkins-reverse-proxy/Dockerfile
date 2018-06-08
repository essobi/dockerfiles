FROM nginx  
MAINTAINER Jouni Kaplas <jouni.kaplas@iki.fi>  
EXPOSE 80  
COPY nginx.conf /etc/nginx/nginx.conf.template  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]

