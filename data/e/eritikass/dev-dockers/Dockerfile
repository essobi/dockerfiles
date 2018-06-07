FROM openjdk:8-jre  
LABEL maintainer="eritikass@gmail.com"  
  
ENV SOLR_VERSION 4.7.2  
ENV SOLR solr-$SOLR_VERSION  
  
RUN curl --retry 3
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz | tar -C
/opt --extract --gzip \  
&& mv /opt/$SOLR /opt/solr \  
&& mv /opt/solr/example /opt/solr/server \  
&& mkdir -p /opt/solr/server/solr \  
&& useradd --home-dir /opt/solr --comment "Solr Server" solr \  
&& chown -R solr:solr /opt/solr/server \  
&& mkdir -p /solr/apps/solr/home \  
&& ln -s /opt/solr/dist/ /solr/apps/solr/home/  
  
USER solr  
  
EXPOSE 8983  
WORKDIR /opt/solr/server  
  
CMD ["java", "-jar", "start.jar"]  

