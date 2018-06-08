# A image with Smartmeter 1.3.0  
FROM develar/java:8u45  
LABEL Description="Tool for performance testing" Version="1.3.1"  
MAINTAINER Radim Daniel Pánek <rdpanek@gmail.com>  
  
# main env  
ENV SMARTMETER_VERSION 1.3.0  
ENV SMARTMETER_DIRECTORY SmartMeter_${SMARTMETER_VERSION}  
ENV SMARTMETER_URL http://smartmeter-
api.etnetera.cz/download/release/${SMARTMETER_VERSION}/linux/full/SmartMeter_${SMARTMETER_VERSION}_linux.tar.gz  
ENV SMARTMETER_PATH /home/${SMARTMETER_DIRECTORY}_linux/  
  
RUN apk update && apk upgrade && apk add \  
ca-certificates \  
curl \  
tar \  
&& \  
  
# Download smartmeter  
cd /home/ && \  
curl -o ${SMARTMETER_DIRECTORY}.tar.gz ${SMARTMETER_URL} && \  
tar -zxvf ${SMARTMETER_DIRECTORY}.tar.gz && rm -rf
${SMARTMETER_DIRECTORY}.tar.gz && \  
  
# Download depending  
cd ${SMARTMETER_PATH}programs/apache-jmeter/lib && \  
  
curl -L -o elasticsearch-5.0.0.jar
"http://central.maven.org/maven2/org/elasticsearch/elasticsearch/5.0.0/elasticsearch-5.0.0.jar"
&& \  
curl -L -o transport-5.0.0.jar
"http://central.maven.org/maven2/org/elasticsearch/client/transport/5.0.0/transport-5.0.0.jar"
&& \  
curl -L -o transport-netty3-client-5.0.0.jar
"http://central.maven.org/maven2/org/elasticsearch/plugin/transport-
netty3-client/5.0.0/transport-netty3-client-5.0.0.jar" && \  
curl -L -o transport-netty4-client-5.0.0.jar
"http://central.maven.org/maven2/org/elasticsearch/plugin/transport-
netty4-client/5.0.0/transport-netty4-client-5.0.0.jar" && \  
curl -L -o reindex-client-5.0.0.jar
"http://central.maven.org/maven2/org/elasticsearch/plugin/reindex-
client/5.0.0/reindex-client-5.0.0.jar" && \  
curl -L -o percolator-client-5.0.0.jar
"http://central.maven.org/maven2/org/elasticsearch/plugin/percolator-
client/5.0.0/percolator-client-5.0.0.jar" && \  
curl -L -o lang-mustache-client-5.0.0.jar
"http://central.maven.org/maven2/org/elasticsearch/plugin/lang-mustache-
client/5.0.0/lang-mustache-client-5.0.0.jar" && \  
curl -L -o hppc-0.7.1.jar
"http://central.maven.org/maven2/com/carrotsearch/hppc/0.7.1/hppc-0.7.1.jar"
&& \  
curl -L -o lucene-core-6.3.0.jar
"http://central.maven.org/maven2/org/apache/lucene/lucene-core/6.3.0/lucene-
core-6.3.0.jar" && \  
curl -L -o log4j-api-2.6.2.jar
"http://central.maven.org/maven2/org/apache/logging/log4j/log4j-api/2.6.2/log4j-api-2.6.2.jar"
&& \  
curl -L -o lucene-queries-6.3.0.jar
"http://central.maven.org/maven2/org/apache/lucene/lucene-
queries/6.3.0/lucene-queries-6.3.0.jar" && \  
curl -L -o lucene-join-6.3.0.jar
"http://central.maven.org/maven2/org/apache/lucene/lucene-join/6.3.0/lucene-
join-6.3.0.jar" && \  
curl -L -o lucene-suggest-6.3.0.jar
"http://central.maven.org/maven2/org/apache/lucene/lucene-
suggest/6.3.0/lucene-suggest-6.3.0.jar" && \  
curl -L -o lucene-highlighter-6.3.0.jar
"http://central.maven.org/maven2/org/apache/lucene/lucene-
highlighter/6.3.0/lucene-highlighter-6.3.0.jar" && \  
curl -L -o lucene-queryparser-6.3.0.jar
"http://central.maven.org/maven2/org/apache/lucene/lucene-
queryparser/6.3.0/lucene-queryparser-6.3.0.jar" && \  
curl -L -o lucene-spatial-6.3.0.jar
"http://central.maven.org/maven2/org/apache/lucene/lucene-
spatial/6.3.0/lucene-spatial-6.3.0.jar" && \  
curl -L -o lucene-sandbox-6.3.0.jar
"http://central.maven.org/maven2/org/apache/lucene/lucene-
sandbox/6.3.0/lucene-sandbox-6.3.0.jar" && \  
curl -L -o netty-all-4.1.6.Final.jar
"http://central.maven.org/maven2/io/netty/netty-all/4.1.6.Final/netty-
all-4.1.6.Final.jar" && \  
curl -L -o log4j-core-2.6.2.jar
"http://central.maven.org/maven2/org/apache/logging/log4j/log4j-core/2.6.2/log4j-core-2.6.2.jar"
&& \  
curl -L -o t-digest-3..1.jar
"http://central.maven.org/maven2/com/tdunning/t-digest/3.1/t-digest-3.1.jar"
&& \  
# Remove old .jar  
rm -rf netty-all-4.0.27.Final.jar && \  
  
# Download Elasticsearch BackendListener  
cd ext/ && \  
curl -L -o ElasticSearchBackendListenerClient.jar "https://github.com/test-
stack/elasticSearchBackendListenerClient/blob/master/out/artifacts/ElasticSearchBackendListenerClient_jar/ElasticSearchBackendListenerClient.jar?raw=true"
&& \  
  
# Download jmeter plugin JSON plugins  
cd /tmp && \  
curl -L -o jpgc-json-2.3.zip https://jmeter-plugins.org/files/packages/jpgc-
json-2.3.zip && unzip jpgc-json-2.3.zip && \  
cp -r lib/* ${SMARTMETER_PATH}programs/apache-jmeter/lib/ && rm -rf
${SMARTMETER_PATH}programs/apache-jmeter/lib/ext/jmeter-plugins-
manager-0.10.jar && \  
rm -rf lib jpgc-json-2.3.zip && \  
  
rm -rf /var/cache/apk/* && \  
apk del \  
ca-certificates \  
curl \  
tar  
  
WORKDIR ${SMARTMETER_PATH}  
ENTRYPOINT ["./SmartMeter.sh", "runTestNonGui"]  

