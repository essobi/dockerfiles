# docker build --rm --no-cache -t solr .  
FROM makuk66/docker-solr:4.10.4  
MAINTAINER "Björn Dieding" <bjoern@xrow.de>  
  
ENV container=docker  
  
COPY ezp-default/ /opt/solr/example/solr/ezp-default/  
COPY collection1/ /opt/solr/example/solr/collection1/  
COPY lib/ /opt/solr/example/solr/lib/  
COPY solr.xml /opt/solr/example/solr/solr.xml  
COPY patch.sh /patch.sh  
  
ENV SOLR_VERSION=4.10.4  
ENV SOLR=solr-$SOLR_VERSION  
ENV SOLR_USER=solr  
  
# Bug https://github.com/docker-solr/docker-
solr/commit/949d6bece4e2ae1189d84210ae0b54b7ba87a37c  
# 5.4 Fix  
RUN sed -i -e 's/#SOLR_PORT=8983/SOLR_PORT=8983/' /opt/solr/bin/solr.in.sh  
# 4.10 Fix  
RUN echo "SOLR_PORT=8983" >> /opt/solr/bin/solr.in.sh  
  
USER root  
RUN chown -R $SOLR_USER:$SOLR_USER /opt/solr /opt/$SOLR  
USER solr  
RUN sh /patch.sh  
# wget
http://localhost:8983/solr/admin/cores?action=CREATE&name=ezpublish&instanceDir=/ezp-
default/conf/&dataDir=data&persist=true&loadOnStartup=true  
CMD ["/opt/solr/bin/solr", "-f"]  

