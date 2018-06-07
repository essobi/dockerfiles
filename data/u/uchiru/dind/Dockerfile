FROM docker:17.06-dind  
  
RUN set -ex &&\  
apk add --no-cache git rsync openssh-client  
  
COPY docker-entrypoint.sh /usr/bin  
  
ENTRYPOINT ["/usr/bin/docker-entrypoint.sh"]  
  

