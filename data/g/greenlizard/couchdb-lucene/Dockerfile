FROM greenlizard/java  
  
MAINTAINER GreenLizard Labs <gabriel@greenlizard.com.br>  
  
ENV COUCHDB_LUCENE_VERSION 1.0.2  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
python \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#  
# Lucene  
#  
# Get the source  
RUN cd /opt && \  
wget https://github.com/rnewson/couchdb-
lucene/archive/v$COUCHDB_LUCENE_VERSION.tar.gz && \  
tar xzf /opt/v$COUCHDB_LUCENE_VERSION.tar.gz  
RUN mv /opt/couchdb-lucene-$COUCHDB_LUCENE_VERSION /opt/couchdb-
lucene-$COUCHDB_LUCENE_VERSION.src  
  
# build couchdb-lucene  
RUN cd /opt/couchdb-lucene-$COUCHDB_LUCENE_VERSION.src && mvn  
RUN cd /opt && tar xvzf /opt/couchdb-
lucene-$COUCHDB_LUCENE_VERSION.src/target/couchdb-
lucene-$COUCHDB_LUCENE_VERSION-dist.tar.gz  
  
# cleanup  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /opt/couchdb-
lucene-$COUCHDB_LUCENE_VERSION.src  
  
RUN adduser --system --disabled-password --home /opt/couchdb-
lucene-$COUCHDB_LUCENE_VERSION \--no-create-home --shell=/bin/bash --group
--gecos "" couchdb  
  
ADD ./opt/start_couch_lucene /opt/start_couch_lucene  
  
RUN sed -e 's/^host=localhost$/host=0.0.0.0/' -i /opt/couchdb-
lucene-$COUCHDB_LUCENE_VERSION/conf/couchdb-lucene.ini  
  
RUN chown -R couchdb:couchdb /opt/couchdb-lucene-$COUCHDB_LUCENE_VERSION  
  
# USER couchdb  
CMD ["/opt/start_couch_lucene"]  
  
EXPOSE 5985

