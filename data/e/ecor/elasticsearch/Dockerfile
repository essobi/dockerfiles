FROM anapsix/alpine-java  
MAINTAINER Ecor Ventures  
  
# Set environment variables  
ENV PKG_NAME elasticsearch  
ENV ELASTICSEARCH_VERSION 5.5.1  
ENV ELASTICSEARCH_PKG $PKG_NAME-$ELASTICSEARCH_VERSION  
ENV ELASTICSEARCH_URL
https://download.elasticsearch.org/$PKG_NAME/release/org/$PKG_NAME/distribution/tar/$PKG_NAME/$ELASTICSEARCH_VERSION/$ELASTICSEARCH_PKG.tar.gz  
  
COPY config ./config  
COPY entrypoint.sh /  
  
# Download Elasticsearch  
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories \  
&& apk add -U curl gosu@testing \  
&& curl -o $ELASTICSEARCH_PKG.tar.gz -sSL
https://artifacts.elastic.co/downloads/elasticsearch/$ELASTICSEARCH_PKG.tar.gz
\  
&& tar -xzf $ELASTICSEARCH_PKG.tar.gz \  
&& rm $ELASTICSEARCH_PKG.tar.gz \  
&& mkdir -p /usr/share/elasticsearch \  
&& mv $ELASTICSEARCH_PKG /usr/share/elasticsearch \  
&& mkdir -p /usr/share/elasticsearch/data /usr/share/elasticsearch/logs
/usr/share/elasticsearch/config/scripts \  
&& adduser -DH -s /sbin/nologin elasticsearch \  
&& chown -R elasticsearch:elasticsearch /usr/share/elasticsearch \  
&& chmod +x /entrypoint.sh \  
&& apk del curl \  
&& rm -rf /var/cache/apk/*  
  
ENV PATH /usr/share/elasticsearch/$ELASTICSEARCH_PKG/bin:$PATH  
  
WORKDIR /usr/share/elasticsearch  
  
VOLUME /usr/share/elasticsearch/data  
  
EXPOSE 9200 9300  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["elasticsearch"]  

