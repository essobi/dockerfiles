FROM redis:4-alpine  
  
LABEL maintainer="Claudio Netto <nettoclaudio@ufrj.br>"  
  
COPY files/redis-ha-sentinel-entrypoint.sh /  
  
COPY files/sentinel.conf.skel /tmp/  
  
RUN apk --update add gettext && \  
rm /var/cache/apk/* && \  
mkdir -p /etc/redis && \  
mv /tmp/sentinel.conf.skel /etc/redis/ && \  
chown -R redis:redis /redis-ha-sentinel-entrypoint.sh /etc/redis && \  
chmod 540 /redis-ha-sentinel-entrypoint.sh  
  
USER redis  
  
ENTRYPOINT [ "/redis-ha-sentinel-entrypoint.sh" ]  

