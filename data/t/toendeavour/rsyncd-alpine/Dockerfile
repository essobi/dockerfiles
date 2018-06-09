FROM alpine:latest  
LABEL maintainer="Marc Mettke <marc@itmettke.de>"  
RUN apk --no-cache add rsync && \  
mkdir -p /config /data /log && \  
mv /etc/rsyncd.conf /config  
  
EXPOSE 873  
VOLUME /data  
VOLUME /config  
VOLUME /log  
  
ENTRYPOINT [ "/usr/bin/rsync", \  
"--daemon", \  
"--no-detach", \  
"--config=/config/rsyncd.conf", \  
"--log-file=/log/rsyncd.log", \  
"--dparam=pidfile=/var/run/rsyncd.pid" \  
]  
HEALTHCHECK CMD /bin/ash -c "PID=\$(cat /var/run/rsyncd.pid) && [ -n
\"\${PID}\" -a -d \"/proc/\${PID}\" ] && exit 0 || exit 1"  

