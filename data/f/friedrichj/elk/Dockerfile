FROM friedrichj/java8  
  
RUN apk add --update curl ca-certificates sudo supervisor && \  
addgroup sudo && \  
echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \  
mkdir /opt  
  
ENV ELASTICSEARCH_VERSION 2.3.4  
RUN curl -Lskj
https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/$ELASTICSEARCH_VERSION/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz
| tar xfz - && \  
mv /elasticsearch-$ELASTICSEARCH_VERSION /opt/elasticsearch && \  
rm -rf $(find /opt/elasticsearch | egrep
"(\\.(exe|bat)$|sigar/.*(dll|winnt|x86-linux|solaris|ia64|freebsd|macosx))")
&& \  
adduser -D -g '' -G sudo -s /sbin/nologin elasticsearch && \  
mkdir -p /data/elasticsearch && \  
chown -R elasticsearch /opt/elasticsearch /data/elasticsearch  
  
ENV LOGSTASH_VERSION 2.3.4  
RUN apk add --no-cache bash libzmq && \  
cd /usr/lib && ln -sf libzmq.so.5 libzmq.so && cd / && \  
curl -Lskj
http://download.elastic.co/logstash/logstash/logstash-$LOGSTASH_VERSION.tar.gz
| tar xfz - && \  
mv logstash-$LOGSTASH_VERSION /opt/logstash && \  
rm -rf $(find /opt/logstash | egrep
"(\\.(exe|bat)$|sigar/.*(dll|winnt|x86-linux|solaris|ia64|freebsd|macosx))")  
  
ENV KIBANA_VERSION 4.5.2-linux-x64  
RUN apk add --no-cache nodejs && \  
curl -s
https://download.elasticsearch.org/kibana/kibana/kibana-${KIBANA_VERSION}.tar.gz
| tar xfz - && \  
mv /kibana-${KIBANA_VERSION} /opt/kibana && \  
rm -rf /opt/kibana/node && \  
mkdir -p /opt/kibana/node/bin && \  
ln -sf /usr/bin/node /opt/kibana/node/bin/node  
  
COPY elasticsearch/* /opt/elasticsearch/config/  
COPY logstash.conf /opt/logstash/config/  
COPY supervisord.conf /etc/  
  
VOLUME ["/data"]  
  
EXPOSE 2120 5601  
ENTRYPOINT [ "/usr/bin/supervisord", "-c", "/etc/supervisord.conf" ]  

