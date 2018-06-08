FROM alpine:3.5  
MAINTAINER Maestrano <it@maestrano.com>  
  
RUN \  
apk add --no-cache ca-certificates && \  
apk add --no-cache --virtual .build-deps curl && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
curl https://dl.minio.io/server/minio/release/linux-amd64/minio >
/usr/bin/minio && \  
chmod +x /usr/bin/minio  
  
EXPOSE 9000  
# Point-in-time backup script with backup rotation  
COPY backup.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/backup.sh  
  
# Entrypoint  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
# Healthcheck  
COPY healthcheck.sh /usr/local/bin/  
HEALTHCHECK \--timeout=5s CMD sh /usr/local/bin/healthcheck.sh  
  
# Data (/export), configuration (/root/.minio) and backup (/snapshots) volumes  
VOLUME ["/export", "/root/.minio", "/snapshots"]  
  
# Start in server mode by default  
CMD ["server","/export"]  

