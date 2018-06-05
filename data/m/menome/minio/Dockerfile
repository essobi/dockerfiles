FROM minio/minio  
  
RUN apk add --update bash && rm -rf /var/cache/apk/*  
# This is just so if we don't have rabbit_host specified it still works.  
ENV RABBIT_HOST=www.google.com:80  
COPY wait-for-it.sh /usr/bin/wait-for-it.sh  
COPY notificationsetting.sh /usr/bin/notificationsetting.sh  
COPY notification.xml /root/notification.xml  
RUN chmod +x /usr/bin/wait-for-it.sh /usr/bin/notificationsetting.sh  
  
ENTRYPOINT /usr/bin/wait-for-it.sh $(echo $RABBIT_HOST) -t 60 --
/usr/bin/docker-entrypoint.sh server /export  

