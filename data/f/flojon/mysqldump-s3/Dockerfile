FROM flojon/s3cmd:2.0.1  
MAINTAINER Jonas Flodén <jonas@koalasoft.se>  
  
RUN apk --no-cache add mysql-client  
  
RUN mkdir /tmp/backup  
WORKDIR /tmp/backup  
  
ADD backup.sh .  
RUN chmod +x backup.sh  
  
ENTRYPOINT [""]  
  
CMD ["/tmp/backup/backup.sh"]  

