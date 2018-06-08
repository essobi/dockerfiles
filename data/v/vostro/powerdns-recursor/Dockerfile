FROM alpine:edge  
  
RUN echo "@community http://dl-cdn.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "@main http://dl-cdn.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
apk add -U --no-cache \  
pdns-recursor@community \  
drill@main && \  
rm -rf /var/cache/apk/*  
  
# Edit recursor.conf  
RUN sed -i "s|daemon=yes|daemon=no|g" /etc/pdns/recursor.conf && \  
sed -i "s|# local-address=127.0.0.1|local-address=0.0.0.0|g"
/etc/pdns/recursor.conf && \  
sed -i "s|# include-dir=|include-dir=/data/recursor-conf.d|g"
/etc/pdns/recursor.conf && \  
sed -i "s|# webserver=no|webserver=yes|g" /etc/pdns/recursor.conf && \  
sed -i "s|# webserver-address=127.0.0.1|webserver-address=0.0.0.0|g"
/etc/pdns/recursor.conf && \  
sed -i "s|# webserver-allow-from=0.0.0.0/0,::/0|webserver-allow-
from=0.0.0.0/0,::/0|g" /etc/pdns/recursor.conf && \  
sed -i "s|# query-local-address6=|query-local-address6=::|g"
/etc/pdns/recursor.conf  
  
# Give ownership of default config file to recursor:recursor  
# This enables runtime zone/script reloading with rec_control  
RUN chown recursor: /etc/pdns/recursor.conf  
  
# Make sure the include-dir always exists  
RUN mkdir -p /data/recursor-conf.d  
  
# Make /data a volume  
VOLUME /data  
  
# Health check  
HEALTHCHECK \--interval=5s --timeout=3s CMD \  
drill health.localhost.tld @localhost | grep -q 'rcode: NXDOMAIN' && \  
drill localhost @localhost | grep -q 'rcode: NOERROR'  
  
COPY entrypoint.sh /  
  
RUN chmod +x /entrypoint.sh  
  
# Run pdns_recursor  
CMD ["/entrypoint.sh"]

