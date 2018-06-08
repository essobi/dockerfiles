from eyjhb/alpine-base  
  
# install packages  
RUN \  
apk add --no-cache \  
rsyslog \  
python && \  
python -m ensurepip && \  
python -m pip install rotate-backups && \  
rm -r /root/.cache && \  
rm -r /usr/lib/python*/ensurepip  
  
# copy root directories  
COPY root/ /  
  
# health checks  
HEALTHCHECK \--interval=90s --timeout=10s --retries=3 \  
CMD /bin/sh /healthcheck.sh  
  
# ports and volumes  
VOLUME ["/config", "/media"]  
  
ENTRYPOINT ["/init"]  

