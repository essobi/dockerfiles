FROM quay.io/letsencrypt/letsencrypt:latest  
  
LABEL maintainer="Takács Ákos <rimelek@it-sziget.hu>"  
  
COPY entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

