FROM alpine:3.2  
RUN apk update && \  
apk add socat curl mysql-client && \  
rm -r /var/cache/  
  
ADD ./entrypoint.sh /entrypoint.sh  
ADD ./json.sh /usr/bin/json  
  
ENV TERM="xterm"  
VOLUME "/config"  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD env | grep 3306_TCP= | sed
's/.*_PORT_\\([0-9]*\\)_TCP=tcp:\/\/\\(.*\\):\\(.*\\)/socat -t 100000000
TCP4-LISTEN:\1,fork,reuseaddr TCP4:\2:\3/' | sh  
  
EXPOSE 3306  

