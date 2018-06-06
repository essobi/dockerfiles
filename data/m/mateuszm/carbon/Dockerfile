FROM python:2.7.12-alpine  
  
MAINTAINER mateuszmoneta@gmail.com  
  
RUN apk update && apk add --no-cache\  
gcc\  
musl-dev\  
&& pip install\  
carbon==1.0.2\  
whisper==1.0.2\  
dumb-init\  
&& apk del gcc musl-dev \  
&& rm -rf /var/cache/apk/* /root/.cache/*  
  
ENV PYTHONPATH=/usr/local/lib/python2.7/site-packages/opt/graphite/lib\  
GRAPHITE_CONF_DIR=/etc/carbon\  
GRAPHITE_STORAGE_DIR=/var/lib/carbon\  
WHISPER_DIR=/var/lib/carbon/whisper\  
CARBON_USER=carbon\  
CARBON_OPTS=""  
RUN mkdir -p $GRAPHITE_CONF_DIR $WHISPER_DIR\  
&& adduser -Ss /bin/sh $CARBON_USER  
  
ONBUILD COPY *.conf $GRAPHITE_CONF_DIR/  
  
COPY carbon-entrypoint.py /carbon-entrypoint.py  
COPY storage-schemas.conf $GRAPHITE_CONF_DIR/storage-schemas.conf  
  
ENTRYPOINT ["dumb-init", "/carbon-entrypoint.sh"]

