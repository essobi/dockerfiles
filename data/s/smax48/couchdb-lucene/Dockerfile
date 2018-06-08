FROM java:8  
ENV CDB_LUCENE_VER 1.0.2  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends maven \  
&& apt-get clean -y \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN cd /opt \  
&& wget https://github.com/rnewson/couchdb-lucene/archive/v$CDB_LUCENE_VER.zip
\  
&& unzip v$CDB_LUCENE_VER.zip \  
&& cd couchdb-lucene-$CDB_LUCENE_VER/ \  
&& mvn \  
&& unzip target/couchdb-lucene-$CDB_LUCENE_VER-dist.zip -d /opt/dist \  
&& cd /opt \  
&& rm -rf couchdb-lucene-$CDB_LUCENE_VER v$CDB_LUCENE_VER.zip  
  
RUN adduser --system --disabled-password --home /opt/dist/couchdb-
lucene-$CDB_LUCENE_VER \--no-create-home --shell=/bin/bash --group --gecos ""
couchdb  
  
COPY ./docker-entrypoint.sh /opt/docker-entrypoint.sh  
  
RUN sed -e 's/^host=localhost$/host=0.0.0.0/' -i /opt/dist/couchdb-
lucene-$CDB_LUCENE_VER/conf/couchdb-lucene.ini  
  
RUN chmod +x /opt/docker-entrypoint.sh \  
&& chown -R couchdb:couchdb /opt/dist/couchdb-lucene-$CDB_LUCENE_VER  
  
WORKDIR /opt/dist/couchdb-lucene-$CDB_LUCENE_VER  
  
EXPOSE 5985  
ENV CDB_AUTH=""  
CMD ["/opt/docker-entrypoint.sh"]

