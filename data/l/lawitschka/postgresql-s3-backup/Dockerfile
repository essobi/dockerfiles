FROM cgswong/aws:aws  
  
# Install PostgreSQL client tools  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
apk update && \  
apk add "postgresql-client@edge<9.7" "postgresql@edge<9.7" && \  
rm -rf /var/cache/apk/*  
  
# Set up backup script  
COPY ./bin/backup.sh /usr/local/bin/backup  
ENTRYPOINT ["/usr/local/bin/backup"]  

