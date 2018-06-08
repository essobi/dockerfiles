FROM onjin/alpine-postgres:9.5  
RUN apk --update add curl  
  
ADD scripts/* /usr/local/bin/  
RUN chmod +x /usr/local/bin/putS3 \  
&& chmod +x /usr/local/bin/confluence.sh \  
&& chmod +x /usr/local/bin/crowd.sh \  
&& chmod +x /usr/local/bin/backup.sh \  
&& chmod +x /usr/local/bin/restore.sh \  
&& chmod +x /usr/local/bin/entrypoint.sh  
  
# Will want to change to a crontab for more control  
RUN ln -s /usr/local/bin/backup.sh /etc/periodic/daily/backup  
  
CMD ["crond", "-f", "-d", "8"]  

