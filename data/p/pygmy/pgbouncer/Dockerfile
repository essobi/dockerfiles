FROM pygmy/alpine-tini:edge  
  
MAINTAINER Maciej Lisiewski <maciej.lisiewski@gmail.com>  
  
RUN apk add --no-cache \  
pgbouncer  
  
ADD entrypoint.sh /entrypoint.sh  
ADD pgbouncer.ini /pgbouncer.ini  
  
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]

