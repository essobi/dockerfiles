FROM alpine:3.6  
WORKDIR /home/app  
  
RUN apk update && apk add openssh && rm -rf /var/cache/apk/*  
  
# Add crontab file in the cron directory  
ADD files/crontab /var/spool/cron/crontabs/root  
  
# Give execution rights on the cron job  
RUN chmod 0600 /var/spool/cron/crontabs/root  
  
# copy the backup script  
COPY files/copyBackup.sh /home/app/  
  
# Run the command on container startup  
CMD crond -l 2 -f  

