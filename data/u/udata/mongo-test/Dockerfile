FROM mongo:3.2.16  
ENV TMPFS_SIZE 1024  
COPY entrypoint.sh /entrypoint.sh  
COPY mongod.conf /etc/mongod.conf  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 27017  
CMD ["mongod", "--config", "/etc/mongod.conf"]  

