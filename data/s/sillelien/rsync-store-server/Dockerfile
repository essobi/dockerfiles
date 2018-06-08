FROM sillelien/base-alpine:0.9.2  
VOLUME /shared  
EXPOSE 873  
COPY build.sh /tmp/build.sh  
RUN chmod 755 /tmp/build.sh  
RUN /tmp/build.sh  
  
COPY rsync.sh /etc/services.d/rsync/run  
COPY cleanup.sh /etc/services.d/cleanup/run  
RUN chmod 755 /etc/services.d/rsync/run /etc/services.d/cleanup/run  

