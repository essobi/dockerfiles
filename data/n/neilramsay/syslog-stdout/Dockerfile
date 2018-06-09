FROM alpine  
  
RUN set -ex && \  
apk --no-cache add python2  
  
COPY syslog-stdout.py daemon.py /usr/local/bin/  

