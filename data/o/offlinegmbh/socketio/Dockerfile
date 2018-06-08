FROM zzrot/alpine-node  
MAINTAINER Tobias Kuendig <tobias@offline.swiss>  
  
RUN apk add --update \  
supervisor \  
&& rm -rf /var/cache/apk/*  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN /bin/mkdir -p /srv/logs  
  
RUN npm install --silent socket.io ioredis  
RUN npm dedupe  
  
WORKDIR /srv  
  
EXPOSE 3000  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  
  

