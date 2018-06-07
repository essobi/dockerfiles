# Create image for a SOLR container  
FROM infotechsoft/java:8-jre  
  
MAINTAINER Ray Bradley "https://github.com/rmbrad"  
ENV SOLR_VERSION 4.10.4  
ENV SOLR solr-$SOLR_VERSION  
ENV SOLR_JETTY /usr/local/$SOLR  
ENV SOLR_HOME /var/lib/solr  
  
RUN yum -y install epel-release && \  
yum -y install jq && \  
DWNLD_URL="http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz"
&& \  
curl -L $DWNLD_URL | \  
tar -xz -C /tmp/ --exclude $SOLR/example/example* --exclude
$SOLR/example/multicore --exclude $SOLR/example/solr/collection1 --strip-
components=1 $SOLR/example && \  
mv /tmp/example $SOLR_JETTY && \  
mv $SOLR_JETTY/solr $SOLR_HOME && \  
mkdir -p /var/log/solr && \  
sed -i 's:^\\(solr.log=\\).*:\1/var/log/solr/:g'
$SOLR_JETTY/resources/log4j.properties && \  
yum -y remove jq && \  
yum -y clean all  
  
EXPOSE 8983  
WORKDIR $SOLR_JETTY  
  
CMD java $JAVA_OPTS -Dsolr.solr.home=/var/lib/solr -jar start.jar  

