FROM alpine:3.7  
LABEL Michel Desconnets "michel.desconnets@gmail.com"  
  
ENV ALLOW_OVERWRITE=on \  
ANONYMOUS_DISABLE=off \  
ANON_UPLOAD_ENABLE=DenyAll \  
FTPUSER_PASSWORD=ftppassword \  
FTPUSER_NAME=ftpuser \  
FTPUSER_UID=1001 \  
LOCAL_UMASK=022 \  
MAX_CLIENTS=10 \  
MAX_INSTANCES=30 \  
PASV_ADDRESS= \  
PASV_MAX_PORT=30100 \  
PASV_MIN_PORT=30091 \  
SERVER_NAME=ProFTPD \  
TIMES_GMT=off \  
TZ=UTC \  
WRITE_ENABLE=AllowAll  
  
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' \  
>>/etc/apk/repositories && \  
apk add --update proftpd@testing tzdata  
COPY proftpd.conf.j2 /etc/proftpd/proftpd.conf  
  
VOLUME /etc/proftpd/conf.d /etc/proftpd/modules.d /var/lib/ftp  
EXPOSE 21 $PASV_MIN_PORT-$PASV_MAX_PORT  
  
COPY entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

