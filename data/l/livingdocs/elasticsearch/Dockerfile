FROM alpine:3.4  
ENV ELASTICSEARCH_VERSION 2.4.5  
ENV PATH $PATH:/usr/share/elasticsearch/bin  
ENV multi__allow_explicit_index=false  
  
COPY fix-permissions /usr/libexec/fix-permissions  
  
RUN \  
apk add --no-cache ca-certificates curl openjdk7-jre-base && \  
  
# install elasticsearch  
adduser -S elasticsearch && \  
  
echo Downloading elasticsearch... && \  
curl -skL
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-$ELASTICSEARCH_VERSION.tar.gz
| tar -xz -C /tmp && \  
mv /tmp/elasticsearch* /usr/share/elasticsearch && \  
mkdir /usr/share/elasticsearch/logs /usr/share/elasticsearch/data && \  
/usr/libexec/fix-permissions /usr/share/elasticsearch && \  
  
# verify  
echo 'JAVA VERSION:' && \  
java -version 2>&1 && \  
  
echo 'ELASTICSEARCH VERSION:' && \  
elasticsearch --version && \  
  
# cleanup  
rm -rf /var/cache/apk/*  
  
COPY start.sh /start.sh  
COPY elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
VOLUME ["/usr/share/elasticsearch/data", "/usr/share/elasticsearch/logs"]  
  
EXPOSE 9200 9300  
USER elasticsearch  
  
ENTRYPOINT ["/start.sh"]  
CMD ["elasticsearch"]  

