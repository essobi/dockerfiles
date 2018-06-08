FROM sillelien/base-alpine:0.9.2  
VOLUME /shared  
  
COPY build.sh /tmp/build.sh  
RUN chmod 755 /tmp/build.sh  
RUN /tmp/build.sh  
  
ENV BACKUP_DAYS 7  
COPY update.sh /etc/services.d/update/run  
COPY cleanup.sh /etc/services.d/cleanup/run  
RUN chmod 755 /etc/services.d/update/run /etc/services.d/cleanup/run  

