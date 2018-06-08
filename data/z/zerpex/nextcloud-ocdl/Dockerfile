FROM hoellen/nextcloud:latest  
  
RUN addgroup -g $GID -S cloud && \  
adduser -u $UID -S cloud -G cloud  
  
# Install aria2  
RUN echo http://dl-2.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories && \  
apk --no-cache add \  
shadow \  
curl \  
php-curl \  
sudo \  
aria2 && \  
mkdir /var/log/aria2c /var/local/aria2c && \  
touch /var/log/aria2c/aria2c.log && \  
touch /var/local/aria2c/aria2c.sess && \  
chown $UID:$GID -R /var/log/aria2c /var/local/aria2c && \  
chmod 770 -R /var/log/aria2c /var/local/aria2c  
  
# Install youtube-dl  
USER root  
RUN apk add -t python && \  
curl -L https://yt-dl.org/downloads/latest/youtube-dl -o
/usr/local/bin/youtube-dl && \  
chmod a+rx /usr/local/bin/youtube-dl  
  
HEALTHCHECK \  
\--interval=30s \  
\--timeout=5s \  
\--retries=3 \  
\--start-period=1m \  
CMD curl -f localhost || exit 1  
  
VOLUME /var/log/aria2c /var/local/aria2c  
  
COPY wrapper_script.sh /usr/local/bin/wrapper_script.sh  
CMD wrapper_script.sh  

