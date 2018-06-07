FROM quay.io/falkonry/openjdk:8-jdk-alpine-zulu  
  
ENV DRILL_VERSION 1.12.0  
ENV DRILL_MAX_DIRECT_MEMORY 8G  
ENV DRILL_HEAP 4G  
ENV DRILL_CLUSTER falkonry  
  
RUN mkdir -p /opt/drill && \  
curl -o apache-drill-${DRILL_VERSION}.tar.gz
http://www.eu.apache.org/dist/drill/drill-${DRILL_VERSION}/apache-
drill-${DRILL_VERSION}.tar.gz && \  
tar -zxpf apache-drill-${DRILL_VERSION}.tar.gz -C /opt/drill && \  
rm apache-drill-${DRILL_VERSION}.tar.gz  
  
ADD dfs.config /dfs.config  
ADD bootstrap-storage-plugins.json /opt/drill/apache-
drill-${DRILL_VERSION}/conf  
ADD start.sh /opt/drill/apache-drill-${DRILL_VERSION}/bin  
ADD update.sh /opt/drill/apache-drill-${DRILL_VERSION}/bin  
ADD logback.xml /opt/drill/apache-drill-${DRILL_VERSION}/conf  
  
ENTRYPOINT /opt/drill/apache-drill-${DRILL_VERSION}/bin/start.sh  
  
EXPOSE 8047  
EXPOSE 31010

