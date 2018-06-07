FROM node:8.11.1-alpine  
  
RUN apk update  
RUN apk add --no-cache logrotate ca-certificates openssl wget build-base  
RUN wget -q https://s3-eu-west-1.amazonaws.com/obs.duel.me/docker-
support/machine-names.list \  
-O /usr/share/machine-names  
  
# Required for VIPS on Alpine Linux.  
RUN apk add vips-dev fftw-dev --update-cache --repository \  
https://dl-3.alpinelinux.org/alpine/edge/testing/  
RUN rm -rf /var/cache/apk/*  
  
# NPM and global modules.  
RUN npm i -g npm@^5.10.0  
RUN npm i -g pm2@^2.10.3  
  
# Papertrail.  
RUN wget -q
https://github.com/papertrail/remote_syslog2/releases/download/v0.20/remote_syslog_linux_amd64.tar.gz
\  
-O release  
RUN tar -xvzf release  
RUN mv remote_syslog/remote_syslog /usr/local/bin  
RUN rm -rf release remote_syslog  
  
CMD ['node']  

