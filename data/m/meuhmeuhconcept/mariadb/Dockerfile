FROM alpine:3.6  
MAINTAINER jn.germon@gmail.com  
  
RUN apk update && \  
apk add \  
mariadb=10.1.26-r0 \  
mariadb-client=10.1.26-r0 \  
logrotate \  
pwgen \  
&& rm -rf /var/cache/apk/*  
  
# make life easier  
ENV TERM xterm  
  
COPY conf/* /etc/mysql/  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
COPY configure-backup-rotate.sh /configure-backup-rotate.sh  
RUN chmod a+x /configure-backup-rotate.sh  
  
COPY cron-logrotate.sh /etc/periodic/daily/logrotate  
RUN chmod a+x /etc/periodic/daily/logrotate  
  
EXPOSE 3306  
ENTRYPOINT ["/entrypoint.sh"]  
  
# demonize  
CMD ["mysqld_safe"]  

