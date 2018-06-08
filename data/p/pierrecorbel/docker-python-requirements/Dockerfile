FROM python:2.7.14  
WORKDIR /app  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod 755 /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

