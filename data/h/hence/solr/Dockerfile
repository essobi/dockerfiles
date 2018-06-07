FROM hence/java:latest  
MAINTAINER Clint Beacock <clint@therefore.ca>  
  
ENV HENCE_APP_NAME=solr \  
HENCE_APP_USER=hence \  
HENCE_APP_VERSION=3.2 \  
SOLR_VERSION=5.2.1  
ENV HENCE_APP_DIR=$HENCE_PREFIX/$HENCE_APP_NAME \  
HENCE_APP_VOL_PREFIX=/hence/$HENCE_APP_NAME \  
SOLR=solr-$SOLR_VERSION  
  
RUN mkdir -p /opt && \  
curl -s --retry 3
http://archive.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz | tar -C
/opt --extract --gzip && \  
ln -s /opt/$SOLR /opt/solr  
  
COPY rootfs /  
  
RUN sh $HENCE_PREFIX/install.sh && \  
s6-rmrf /etc/s6/services/s6-fdholderd/down  
  
EXPOSE 8983  
VOLUME ["$HENCE_APP_VOL_PREFIX/conf", "$HENCE_APP_VOL_PREFIX/data",
"$HENCE_APP_VOL_PREFIX/logs/solr-general-logs",
"$HENCE_APP_VOL_PREFIX/logs/solr-error-logs"]  
  
WORKDIR /opt/solr  

