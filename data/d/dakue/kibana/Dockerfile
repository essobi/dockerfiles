FROM alpine:latest  
MAINTAINER Daniel Kühne <dkhmailto@googlemail.com>  
  
ENV KIBANA_VERSION 4.4.1  
RUN set -x && \  
apk --update add curl tar && \  
mkdir -p /opt/kibana && \  
curl -sS -L
https://download.elasticsearch.org/kibana/kibana/kibana-${KIBANA_VERSION}-linux-x64.tar.gz
| \  
tar xz --strip-components=1 -C /opt/kibana && \  
apk add nodejs && \  
rm -rf /opt/kibana/node && \  
mkdir -p /opt/kibana/node/bin && \  
ln -sf /usr/bin/node /opt/kibana/node/bin/node && \  
apk del curl tar && \  
rm /var/cache/apk/*  
  
RUN set -x && \  
/opt/kibana/bin/kibana plugin -i kibana/timelion && \  
/opt/kibana/bin/kibana plugin -i elastic/sense  
  
ADD ./docker-entrypoint.sh /docker-entrypoint.sh  
  
EXPOSE 5601  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["kibana"]  

