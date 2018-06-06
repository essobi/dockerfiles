FROM certbot/certbot  
MAINTAINER DylanWu  
  
ENV DOMAIN=  
ENV EMAIL=  
ENV USE_SAN false  
EXPOSE 80 443  
COPY docker-entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  

