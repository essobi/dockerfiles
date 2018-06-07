FROM alpine:3.7  
RUN apk add --no-cache bash openssl curl python python-dev py-pip build-base
librsync-dev rsync lftp gnupg zabbix-utils  
  
ENV DUPLICITY_VERSION="0.7.17"  
ENV DUPLICITY="duplicity-$DUPLICITY_VERSION"  
RUN wget -qO /tmp/${DUPLICITY}.tar.gz
https://code.launchpad.net/duplicity/0.7-series/${DUPLICITY_VERSION}/+download/${DUPLICITY}.tar.gz
\  
&& pip install /tmp/${DUPLICITY}.tar.gz boto urllib3 \  
&& rm /tmp/${DUPLICITY}.tar.gz  
  
COPY duplicity-backup.sh /duplicity-backup.sh  
RUN chmod +x /duplicity-backup.sh  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
CMD ["/docker-entrypoint.sh"]  

