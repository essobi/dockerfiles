FROM maven:3-jdk-8  
# File Author / Maintainer  
MAINTAINER Toni Hermoso Pulido <toniher@cau.cat>  
# Adapted from https://github.com/klaemo/docker-couchdb-
lucene/blob/master/Dockerfile  
ARG COUCHDB_LUCENE_VERSION=2.0.0  
ENV COUCHDB_PORT 5984  
ENV COUCHDB_SERVER couchdb  
  
RUN groupadd -r couchdb && useradd -d /opt/couchdb-lucene -g couchdb couchdb  
  
RUN mkdir -p /usr/src; cd /usr/src \  
&& curl -L https://github.com/rnewson/couchdb-
lucene/archive/v$COUCHDB_LUCENE_VERSION.tar.gz | tar -xz \  
&& cd couchdb-lucene-$COUCHDB_LUCENE_VERSION \  
&& mvn  
RUN cd /usr/src/couchdb-lucene-$COUCHDB_LUCENE_VERSION/target \  
&& unzip couchdb-lucene-$COUCHDB_LUCENE_VERSION-dist.zip \  
&& mv couchdb-lucene-$COUCHDB_LUCENE_VERSION /opt/couchdb-lucene \  
&& rm -rf /usr/src/couchdb-lucene-*  
  
COPY run-lucene.sh /opt/couchdb-lucene/run-lucene.sh  
RUN chmod +x /opt/couchdb-lucene/run-lucene.sh  
  
WORKDIR /opt/couchdb-lucene  
EXPOSE 5985  
VOLUME ["/opt/couchdb-lucene/indexes"]  
  
ENTRYPOINT ["./run-lucene.sh"]  

