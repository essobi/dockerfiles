# Base image:  
FROM golang:1.9-alpine  
  
RUN echo http://nl.alpinelinux.org/alpine/v3.4/community >>
/etc/apk/repositories  
RUN apk add --no-cache mysql-client openssl git nfs-utils openssh fuse  
  
RUN git clone https://github.com/restic/restic \  
&& cd restic \  
&& go run build.go \  
&& cp restic /usr/local/bin/  
RUN apk del git  
  
ADD . /backup  
  
WORKDIR /backup  
  
RUN mkdir -p /backup/backups  
  
RUN echo "0 3 * * * /backup/backup.sh > /dev/stdout" > /etc/crontabs/root  
  
CMD crond -l 2 -f  

