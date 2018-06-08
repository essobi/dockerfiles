  
FROM openjdk:8-jre  
MAINTAINER Kevin Risden "risdenk@avalonconsult.com"  
RUN apt-get update && \  
apt-get -y install lsof && \  
rm -rf /var/lib/apt/lists/*  
  
ENV SOLR_USER solr  
ENV SOLR_UID 8983  
RUN groupadd -r $SOLR_USER && \  
useradd -r -u $SOLR_UID -g $SOLR_USER $SOLR_USER  
  
ENV SOLR_VERSION 8.0.0-3331  
RUN mkdir -p /opt/solr && \  
wget -nv --output-document=/opt/solr.tgz https://builds.apache.org/job/Solr-
Artifacts-
master/lastSuccessfulBuild/artifact/solr/package/solr-$SOLR_VERSION.tgz && \  
tar -C /opt/solr --extract --file /opt/solr.tgz --strip-components=1 && \  
rm /opt/solr.tgz* && \  
mkdir -p /opt/solr/server/solr/lib && \  
sed -i -e 's/#SOLR_PORT=8983/SOLR_PORT=8983/' /opt/solr/bin/solr.in.sh && \  
sed -i -e '/-Dsolr.clustering.enabled=true/ a SOLR_OPTS="$SOLR_OPTS
-Dsun.net.inetaddr.ttl=60 -Dsun.net.inetaddr.negative.ttl=60"'
/opt/solr/bin/solr.in.sh && \  
chown -R $SOLR_USER:$SOLR_USER /opt/solr && \  
mkdir /docker-entrypoint-initdb.d /opt/docker-solr/  
  
COPY scripts /opt/docker-solr/scripts  
RUN chmod -R a+x /opt/docker-solr/scripts/docker-entrypoint.sh  
RUN chown -R $SOLR_USER:$SOLR_USER /opt/docker-solr  
  
EXPOSE 8983  
WORKDIR /opt/solr  
USER $SOLR_USER  
  
ENTRYPOINT ["/opt/docker-solr/scripts/docker-entrypoint.sh"]  
CMD ["solr-foreground"]  

