FROM delitescere/java  
  
# Export HTTP & Transport  
EXPOSE 9200 9300  
ENV VERSION 5.0.0-alpha1  
  
  
# Install Elasticsearch.  
RUN apk add --update tar curl ca-certificates sudo && \  
mkdir /elasticsearch && cd /elasticsearch && \  
( curl -Lskj
https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/$VERSION/elasticsearch-$VERSION.tar.gz
| \  
gunzip -c - | tar xf - --strip 1 ) && \  
rm -rf $(find /elasticsearch | egrep
"(\\.(exe|bat)$|sigar/.*(dll|winnt|x86-linux|solaris|ia64|freebsd|macosx))")
&& \  
apk del curl wget ca-certificates && \  
mkdir -p /elasticsearch/plugins && mkdir -p /data && chown -R nobody:nobody
/data && \  
/elasticsearch/bin/elasticsearch --version && \  
rm -rf /tmp/* /var/cache/apk/*  
  
# Copy configuration  
COPY config /elasticsearch/config  
COPY docker-entrypoint.sh /elasticsearch/bin/start.sh  
  
# Volume for Elasticsearch data  
VOLUME ["/data"]  
  
ENTRYPOINT [ "/elasticsearch/bin/start.sh" ]  

