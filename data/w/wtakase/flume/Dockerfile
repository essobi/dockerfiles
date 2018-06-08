FROM java:8-jre  
MAINTAINER wtakase <wataru.takase@kek.jp>  
  
ENV FLUME_VERSION 1.6.0  
ENV ELASTICSEARCH_VERSION 1.7.5  
ENV ELASTICSEARCH_REPO_BASE
http://packages.elasticsearch.org/elasticsearch/1.7/debian  
  
RUN mkdir /opt/flume && \  
cd /opt/flume && \  
curl -O http://archive.apache.org/dist/flume/${FLUME_VERSION}/apache-
flume-${FLUME_VERSION}-bin.tar.gz && \  
tar zxf apache-flume-${FLUME_VERSION}-bin.tar.gz --strip 1 && \  
rm -f apache-flume-${FLUME_VERSION}-bin.tar.gz  
  
RUN echo "deb ${ELASTICSEARCH_REPO_BASE} stable main" >
/etc/apt/sources.list.d/elasticsearch.list && \  
apt-get update && \  
apt-get install -y binutils && \  
apt-get install -y --force-yes -d elasticsearch=${ELASTICSEARCH_VERSION} && \  
mkdir /tmp/elasticsearch && cd /tmp/elasticsearch && \  
ar p /var/cache/apt/archives/elasticsearch_${ELASTICSEARCH_VERSION}_all.deb
data.tar.gz | tar zx && \  
cp usr/share/elasticsearch/lib/elasticsearch-*.jar /opt/flume/lib/ && \  
cp usr/share/elasticsearch/lib/lucene-core-*.jar /opt/flume/lib/ && \  
rm -rf /var/lib/apt/lists/* && rm -rf /tmp/elasticsearch && \  
rm -f /var/cache/apt/archives/*.deb  
  
RUN touch /opt/flume/conf/flume.conf  
  
COPY run.sh /  
CMD ["/run.sh"]  

