FROM lochnair/base:alpine  
  
LABEL Description="Docker image for Aria2-WebUI"  
  
RUN \  
apk add \  
\--no-cache \  
\--update \  
aria2 \  
nginx \  
gzip \  
tar && \  
rm -rf /etc/nginx  
  
RUN \  
curl -L -o "/tmp/webui.tar.gz" "https://github.com/ziahamza/webui-
aria2/archive/master.tar.gz" && \  
tar --strip-components=1 -xzf "/tmp/webui.tar.gz" -C "/app" && \  
rm "/tmp/webui.tar.gz" && \  
rm -f /app/*.md && \  
rm -f /app/*Dockerfile && \  
rm -f /app/docker-compose.yml && \  
rm -rf /app/LICENSE && \  
rm -f /app/*.spec && \  
rm -rf /app/screenshots && \  
find /app -type f -not -name "configuration.js" -exec gzip -q -9 -k {} \;  
  
VOLUME /config  
VOLUME /downloads  
  
COPY root/ /

