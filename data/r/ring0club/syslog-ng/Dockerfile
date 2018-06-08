FROM ring0club/python:2.7.15-r0  
RUN apk add syslog-ng=3.13.2-r3 \  
\--repository https://nl.alpinelinux.org/alpine/edge/main \  
\--no-cache  
#VOLUME /etc/syslog-ng  
ENTRYPOINT ["syslog-ng", "--foreground"]  

