FROM limed/alpine-base  
MAINTAINER limed@sudoers.org  
  
COPY files/s3-backup /app/backup  
  
ENV BACKUP_PATH /backups/  
ENV BACKUP_BUCKET backup-bucket  
  
RUN pip install -U awscli\  
&& ln -s /app/backup /etc/periodic/daily/backup\  
&& mkdir -p /backups\  
&& rm -rf /var/cache/apk/*  
  
VOLUME /backups  
CMD [ "/usr/sbin/crond", "-f", "-d", "8"]  

