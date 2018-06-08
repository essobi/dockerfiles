FROM makuk66/docker-solr  
MAINTAINER Mike Graves <mgraves@mit.edu>  
  
USER root  
  
ENV PATH /opt/solr/bin:${PATH}  
ENV SOLR_HOME /var/solr/data/  
ENV OA_CORE ${SOLR_HOME}oastats/  
  
RUN mkdir -p ${OA_CORE}  
RUN mkdir -p ${OA_CORE}conf  
RUN mkdir -p ${OA_CORE}data  
  
ADD solr.xml ${SOLR_HOME}  
ADD core.properties ${OA_CORE}  
ADD solrconfig.xml ${OA_CORE}conf/  
ADD schema.xml ${OA_CORE}conf/  
  
CMD ["sh", "-c", "solr start -f"]  

