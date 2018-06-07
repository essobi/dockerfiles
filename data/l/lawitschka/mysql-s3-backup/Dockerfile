FROM cgswong/aws:aws  
  
# Install PostgreSQL client tools  
RUN apk update && \  
apk add mariadb-client && \  
rm -rf /var/cache/apk/*  
  
# Set up backup script  
COPY ./bin/backup.sh /usr/local/bin/backup  
ENTRYPOINT ["/usr/local/bin/backup"]  

