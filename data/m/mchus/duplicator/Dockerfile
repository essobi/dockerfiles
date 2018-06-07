FROM alpine:3.6  
LABEL maintainer="Mikhail Chusavitin chusavitin@gmail.com"  
LABEL version="1.2.1"  
# Install rsync, dcron and util-linux for flock  
RUN apk update \  
&& apk upgrade \  
&& apk add --no-cache \  
rsync \  
dcron \  
util-linux \  
&& rm -rf /var/cache/apk/*  
  
#create data dirs  
RUN mkdir -p /data/from \  
&& mkdir -p /data/to  
  
#some cron stuff  
RUN mkdir -p /var/log/cron \  
&& mkdir -m 0644 -p /var/spool/cron/crontabs \  
&& touch /var/log/cron/cron.log \  
&& mkdir -m 0644 -p /etc/cron.d  
  
#add crontab record for rsync script  
RUN crontab -l | { cat; echo "* * * * * /usr/bin/flock -n /.sync_lock -c
\"/usr/bin/rsync --exclude '.Trashes' --exclude '.Spotlight-V100' --exclude
'.fseventsd' --checksum --archive --delete /data/from/ /data/to/\""; } |
crontab -  
  
#define volume mounts  
VOLUME /data/from  
VOLUME /data/to  
  
#3.2.1. launch  
CMD crond -s /var/spool/cron/crontabs -b -L /var/log/cron/cron.log "$@" &&
tail -f /var/log/cron/cron.log  

