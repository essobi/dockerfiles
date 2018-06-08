FROM mongo  
  
RUN apt-get update && apt-get install -y wget  
  
ENV RESTORE_URL ""  
RUN rm -f /usr/local/bin/docker-entrypoint.sh  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 27017  
CMD ["mongod"]  

