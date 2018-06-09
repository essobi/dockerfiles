FROM openjdk:jre-alpine  
  
ENV SOLR_VERSION=5.4.1 \  
SOLR_USER=solr \  
SOLR_UID=8983 \  
PATH=/opt/solr/bin:/opt/docker-solr/scripts:$PATH  
  
COPY scripts /opt/docker-solr/scripts  
  
RUN apk add --no-cache \  
lsof \  
gnupg \  
procps \  
tar \  
bash \  
&& apk add --no-cache ca-certificates curl \  
&& update-ca-certificates \  
&& addgroup -S -g $SOLR_UID $SOLR_USER \  
&& adduser -S -u $SOLR_UID -g $SOLR_USER $SOLR_USER \  
&& mkdir -p /opt/solr \  
&& curl -s -L -o /opt/solr.tgz
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/solr-$SOLR_VERSION.tgz
\  
&& tar -C /opt/solr --extract --file /opt/solr.tgz --strip-components=1 \  
&& rm /opt/solr.tgz* \  
&& rm -Rf /opt/solr/docs/ \  
&& sed -i -e 's/#SOLR_PORT=8983/SOLR_PORT=8983/' /opt/solr/bin/solr.in.sh \  
&& sed -i -e '/-Dsolr.clustering.enabled=true/ a SOLR_OPTS="$SOLR_OPTS
-Dsun.net.inetaddr.ttl=60 -Dsun.net.inetaddr.negative.ttl=60"'
/opt/solr/bin/solr.in.sh \  
&& mkdir -p /opt/solr/server/solr/lib /opt/solr/server/solr/mycores
/opt/docker-solr /docker-entrypoint-initdb.d \  
&& chown -R $SOLR_USER:$SOLR_USER /opt/solr /opt/docker-solr  
  
WORKDIR /opt/solr  
USER $SOLR_USER  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["solr-foreground"]  

