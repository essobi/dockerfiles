FROM python:2.7.12-alpine  
  
MAINTAINER Mateusz Moneta <mateuszmoneta@gmail.com>  
  
RUN apk --no-cache add \  
linux-headers \  
build-base \  
&& pip install diamond==4.0.451 statsd==3.2.1 \  
&& apk del \  
build-base \  
linux-headers \  
&& rm -rf /var/cache/apk/*  
  
ENV HANDLERS=diamond.handler.stats_d.StatsdHandler \  
GRAPHITE_HOST=127.0.0.1 \  
GRAPHITE_PORT=2003 \  
STATSD_HOST=127.0.0.1 \  
STATSD_PORT=8125 \  
INTERVAL=10 \  
PATH_PREFIX=''\  
DIAMOND_CONF=/etc/diamond/diamond.conf \  
COLLECTORS_CONF_DIR=/etc/diamond/collectors/ \  
COLLECTORS_DIR=/usr/local/share/diamond/collectors/ \  
HANDLERS_CONF_DIR=/etc/diamond/handlers/ \  
HANDLERS_DIR=/usr/local/share/diamond/handlers/  
  
COPY diamond.conf $DIAMOND_CONF  
COPY entrypoint.py /entrypoint.py  
  
RUN adduser -S diamond \  
&& mkdir -p \  
$COLLECTORS_DIR \  
$HANDLERS_DIR \  
$COLLECTORS_CONF_DIR \  
$HANDLERS_CONF_DIR \  
&& chown -R diamond /usr/local/share/diamond /etc/diamond  
  
  
USER diamond  
ENTRYPOINT ["/entrypoint.py"]  

