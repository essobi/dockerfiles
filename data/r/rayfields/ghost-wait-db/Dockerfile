FROM ghost  
MAINTAINER rayfields  
  
RUN \  
apt-get update && \  
apt-get install -y netcat  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY wait-db.sh /wait-db.sh  
RUN chmod +x /wait-db.sh  
  
ENV DB_HOST=db  
ENV DB_PORT=3306  
ENTRYPOINT ["/wait-db.sh"]  
  
CMD ["npm", "start"]  

