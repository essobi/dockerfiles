FROM alpine:3.3  
ENV ES_VERSION=2.3.1 KIBANA_VERSION=4.5.0-linux-x64 LOGSTASH_VERSION=2.3.2  
RUN apk add \--update openjdk8-jre curl wget bash supervisor nodejs && \  
mkdir -p /opt /var/log/supervisor /var/log/elasticsearch /data /logs && \  
curl -s
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/$ES_VERSION/elasticsearch-$ES_VERSION.tar.gz
| tar -xz -C /opt && \  
ln -s elasticsearch-$ES_VERSION /opt/elasticsearch && \  
curl -s
https://download.elastic.co/kibana/kibana/kibana-$KIBANA_VERSION.tar.gz | tar
-zx -C /opt && \  
ln -s kibana-$KIBANA_VERSION /opt/kibana && \  
rm -rf /opt/kibana/node && \  
mkdir -p /opt/kibana/node/bin && \  
ln -sf /usr/bin/node /opt/kibana/node/bin/node && \  
curl -Ls
https://download.elastic.co/logstash/logstash/logstash-$LOGSTASH_VERSION.tar.gz
| tar -zx -C /opt && \  
ln -sf logstash-$LOGSTASH_VERSION /opt/logstash && \  
rm -fr /var/cache/apk/*  
ADD etc /etc  
RUN chown -R 0:0 /etc  
EXPOSE 80 514 8080 8081 9200 9300 12201  
VOLUME /data /logs  
ENTRYPOINT ["/usr/bin/supervisord", "-n", "-c",
"/etc/supervisor/supervisord.conf"]  

