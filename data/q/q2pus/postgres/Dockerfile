FROM postgres:10-alpine  
  
RUN apk add --update git openssh-client busybox-suid && rm -rf
/var/cache/apk/*  
RUN sed -i '/exec su-exec postgres/i \\\tcrond -f -d 8 &'
/usr/local/bin/docker-entrypoint.sh  
  
COPY ssh-config /ssh-config  
COPY auto-post-provisioning.sh /docker-entrypoint-initdb.d/auto-post-
provisioning.sh  

