FROM alpine:3.5  
LABEL org.freenas.interactive="false" \  
org.freenas.version="10.1.22" \  
org.freenas.upgradeable="false" \  
org.freenas.expose-ports-at-host="true" \  
org.freenas.autostart="true" \  
org.freenas.port-mappings="3306:3306/tcp" \  
org.freenas.volumes="[ \  
{ \  
\"name\": \"/var/lib/mysql\", \  
\"descr\": \"Database storage\" \  
} \  
]" \  
org.freenas.settings="[ \  
{ \  
\"env\": \"MARIADB_ROOT_PASSWORD\", \  
\"descr\": \"Root password\", \  
\"optional\": false \  
}, \  
{ \  
\"env\": \"MARIADB_DATABASE\", \  
\"descr\": \"Database Name\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MARIADB_USER\", \  
\"descr\": \"Optional Admin User\", \  
\"optional\": true \  
}, \  
{ \  
\"env\": \"MARIADB_PASSWORD\", \  
\"descr\": \"Optional Admin User password\",\  
\"optional\": true \  
} \  
]"  
  
WORKDIR /root  
ENV TERM xterm  
  
RUN apk add --no-cache ca-certificates \  
curl \  
bash \  
bash-completion \  
binutils \  
ncurses && \  
adduser -h /var/lib/mysql -s /bin/bash -S mysql && \  
apk add --no-cache \  
mariadb \  
mariadb-client \  
su-exec \  
s6 && \  
rm -rf \  
/var/cache/apk/* \  
/etc/mysql/* \  
/var/lib/mysql/*  
  
ADD rootfs /  
CMD ["/bin/s6-svscan", "/etc/s6"]  

