FROM nephatrine/base-alpine:latest  
LABEL maintainer="Daniel Wolf <nephatrine@gmail.com>"  
  
RUN echo "====== RUNTIME CONFIGURATION ======" \  
&& apk --update upgrade \  
&& apk add \  
libc6-compat \  
mongodb \  
openjdk8-jre \  
\  
&& echo "====== INSTALL UNIFI ======" \  
&& cd /usr/src \  
&& wget "http://www.ubnt.com/downloads/unifi/$(wget -q -O-
https://community.ubnt.com/ubnt/rss/board?board.id=Blog_UniFi | grep -Eo
'UniFi [0-9\\.]+ LTS Stable has' | awk '{print $2}' | head -1)/UniFi.unix.zip"
\  
&& unzip /usr/src/UniFi.unix.zip -d /srv && mv /srv/UniFi /srv/unifi \  
&& unlink /srv/unifi/bin/mongod && ln -s /usr/bin/mongod_wrapper
/srv/unifi/bin/mongod \  
\  
&& echo "====== CLEANUP ======" \  
&& cd /usr/src \  
&& rm -rf \  
/tmp/* \  
/usr/src/* \  
/var/cache/apk/*  
  
EXPOSE 8080/tcp 8443/tcp 8880/tcp 8843/tcp 6789/tcp 3478/udp 10001/udp  
COPY override /

