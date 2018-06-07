FROM greatbsky/openjdk:latest  
MAINTAINER architect.bian  
LABEL name="solr" license="MIT" build-date="20170223"  
  
ENV VERSION 6.4.1  
ENV SOLR_USER solr  
ENV SOLR_GROUP solr  
  
RUN groupadd -r $SOLR_GROUP && useradd -r -g $SOLR_GROUP $SOLR_USER && yum
update -y && cd /data/softs && wget
http://apache.mirrors.pair.com/lucene/solr/$VERSION/solr-$VERSION.tgz && tar
-zxf solr-$VERSION.tgz && mv solr-$VERSION /data/env/solr && chown -R
solr:solr /data/env/solr && sed -i -e 's/#SOLR_PORT=8983/SOLR_PORT=8983/'
/data/env/solr/bin/solr.in.sh && rm -rf /data/softs/*  
  
EXPOSE 8983  
WORKDIR /data/env/solr  
USER $SOLR_USER  
  
CMD ["bin/solr", "start", "-c", "-f"]

