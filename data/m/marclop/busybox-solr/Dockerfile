FROM jeanblanchard/busybox-java:8  
MAINTAINER Marc Lopez <marc5.12@outlook.com>  
  
ENV SOLR_VERSION 4.5.1  
ENV SOLR solr-$SOLR_VERSION  
ENV SOLR_USER solr  
  
# Add user without password  
RUN adduser -D $SOLR_USER && \  
wget -q -O /opt/$SOLR.tgz
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz && \  
gunzip /opt/$SOLR.tgz && tar -x -C /opt -f /opt/$SOLR.tar && \  
rm /opt/$SOLR.tar && \  
ln -s /opt/$SOLR /opt/solr && \  
chown -R $SOLR_USER:$SOLR_USER /opt/solr /opt/$SOLR && \  
mv /opt/solr/example /opt/solr/server  
  
EXPOSE 8983  
WORKDIR /opt/solr/server  
USER $SOLR_USER  
  
ENTRYPOINT ["java", "-jar", "start.jar"]  

