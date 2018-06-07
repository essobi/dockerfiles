FROM dkruger/rsync-cron:latest  
  
### install curl wget bash  
RUN apk add --update coreutils \  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  
  
RUN rm -f /entrypoint.d/rsync.sh  
  
COPY ./rsync-entrypoint.sh /entrypoint.d/rsync.sh  
COPY ./run-rsync.sh /run-rsync.sh

