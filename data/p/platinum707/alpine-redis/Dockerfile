FROM platinum707/alpine-base  
MAINTAINER dockerlite@gmail.com  
  
ENV REDIS_USER=redis \  
REDIS_DATA_DIR=/var/lib/redis \  
REDIS_LOG_DIR=/var/log/redis  
  
# Install redis  
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.6/main" >>
/etc/apk/repositories && \  
apk add --update redis=3.2.8-r0 && \  
apk add --update bash=4.3.48-r1 && \  
apk add --update openrc=0.24.1-r2 && \  
rm -rf /var/cache/apk/* && \  
echo -e "include /etc/redis-local.conf\n" >> /etc/redis.conf  
  
RUN sed 's/^daemonize yes/daemonize no/' -i /etc/redis.conf && \  
sed 's/^bind 127.0.0.1/bind 0.0.0.0/' -i /etc/redis.conf && \  
sed 's/^# unixsocket /unixsocket /' -i /etc/redis.conf && \  
sed 's/^# unixsocketperm 755/unixsocketperm 777/' -i /etc/redis.conf && \  
sed '/^logfile/d' -i /etc/redis.conf  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
# Add the files  
ADD root /  
  
VOLUME ["${REDIS_DATA_DIR}"]  
  
# Expose the ports for redis  
EXPOSE 6379/tcp  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

