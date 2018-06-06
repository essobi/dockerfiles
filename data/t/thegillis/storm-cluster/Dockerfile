FROM java:8-jre  
  
# 0.10.0  
ENV STORM_VERSION 0.9.2-incubating  
ENV APACHE_MIRROR http://apache.cs.utah.edu/storm  
  
RUN apt-get update && apt-get install -y python  
  
RUN curl -o /opt/apache-storm.tar.gz ${APACHE_MIRROR}/apache-
storm-${STORM_VERSION}/apache-storm-${STORM_VERSION}.tar.gz && \  
tar -C /opt -xzf /opt/apache-storm.tar.gz && \  
rm /opt/apache-storm.tar.gz && \  
mv /opt/apache-storm-${STORM_VERSION} /opt/apache-storm && \  
mkdir -p /opt/apache-storm/storm-local && \  
mkdir -p /opt/apache-storm/logs && \  
mkdir -p /opt/apache-storm/logback-dist && \  
mkdir -p /opt/apache-storm/conf-dist && \  
mv /opt/apache-storm/logback/cluster.xml /opt/apache-storm/logback-
dist/cluster-file.xml && \  
cp /opt/apache-storm/conf/* /opt/apache-storm/conf-dist/  
  
COPY logback-cluster.xml /opt/apache-storm/logback/cluster.xml  
COPY logback-cluster.xml /opt/apache-storm/logback-dist/cluster-console.xml  
COPY configure-zookeeper-servers /configure-zookeeper-servers  
COPY run.sh /run.sh  
  
WORKDIR /opt/apache-storm  
  
# see https://github.com/apache/storm/blob/master/SECURITY.md  
EXPOSE 6700 6701 6702 6703 8080 6627  
VOLUME ["/opt/apache-storm/conf", "/opt/apache-storm/logback", "/opt/apache-
storm/logs", "/opt/apache-storm/storm-local"]  
  
CMD ["/run.sh"]  
  

