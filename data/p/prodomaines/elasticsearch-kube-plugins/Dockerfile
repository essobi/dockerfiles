FROM openjdk:8u92-jre-alpine  
  
EXPOSE 9200 9300  
ENV VERSION 2.4.1  
# Install Elasticsearch.  
RUN apk add --update curl ca-certificates sudo && \  
( curl -Lskj
https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/$VERSION/elasticsearch-$VERSION.tar.gz
| \  
gunzip -c - | tar xf - ) && \  
mv /elasticsearch-$VERSION /elasticsearch && \  
rm -rf $(find /elasticsearch | egrep
"(\\.(exe|bat)$|sigar/.*(dll|winnt|x86-linux|solaris|ia64|freebsd|macosx))")
&& \  
apk del curl  
  
# Volume for Elasticsearch data  
VOLUME ["/data"]  
  
COPY config /elasticsearch/config  
  
# Set environment variables defaults  
ENV ES_HEAP_SIZE 512m  
ENV CLUSTER_NAME elasticsearch-default  
ENV NODE_MASTER true  
ENV NODE_DATA true  
ENV HTTP_ENABLE true  
ENV NETWORK_HOST _site_  
ENV HTTP_CORS_ENABLE true  
ENV HTTP_CORS_ALLOW_ORIGIN *  
ENV NUMBER_OF_MASTERS 1  
ENV NUMBER_OF_SHARDS 1  
ENV NUMBER_OF_REPLICAS 0  
# Override elasticsearch.yml config, otherwise plug-in install will fail  
ADD do_not_use.yml /elasticsearch/config/elasticsearch.yml  
  
# Install Elasticsearch plug-ins  
RUN /elasticsearch/bin/plugin install io.fabric8/elasticsearch-cloud-
kubernetes/$VERSION \--verbose && \  
/elasticsearch/bin/plugin install jettro/elasticsearch-gui --verbose && \  
/elasticsearch/bin/plugin install lmenezes/elasticsearch-kopf/v2.1.2 --verbose
&&\  
/elasticsearch/bin/plugin install license --verbose && \  
/elasticsearch/bin/plugin install marvel-agent --verbose  
  
# Override elasticsearch.yml config, otherwise plug-in install will fail  
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Copy run script  
COPY run.sh /  
CMD ["/run.sh"]  

