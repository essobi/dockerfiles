FROM nginx:1.9  
MAINTAINER Matthias Neugebauer <mtneug@mailbox.org>  
  
COPY config /config  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["nginx", "-g", "daemon off;"]  

