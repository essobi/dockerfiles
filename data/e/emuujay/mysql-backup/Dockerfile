FROM alpine:latest  
  
RUN apk add --update bash mysql-client \  
&& rm -rf /var/cache/apk/*  
  
ENV BACKUP_TIME 0 3 * * *  
  
COPY entrypoint.sh /entrypoint.sh  
  
VOLUME /backup  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/sbin/crond", "-f", "-d", "0"]  

