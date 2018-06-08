FROM solr:7.0.0  
MAINTAINER Paul Baptista <pbaptist@uni-bonn.de>  
  
  
# ----------------- #  
# Configuration #  
# ----------------- #  
USER root  
  
# increase heap mem limit  
RUN sed -i 's/#SOLR_HEAP=".*"/SOLR_HEAP="2048m"/' /opt/solr/bin/solr.in.sh &&
\  
sed -i 's/#SOLR_JAVA_MEM=".*"/SOLR_JAVA_MEM="-Xms2048m -Xmx2048m"/'
/opt/solr/bin/solr.in.sh  
  
# add configuration for SlideWiki core  
ADD ./solr-config/ /opt/solr/server/solr  
  
# data directory for swikcore needs special owner to be accessible for solr
user  
RUN mkdir /solr-data && chown -R 8983:8983 /opt/solr/server/solr && chown -R
8983:8983 /solr-data  
  
VOLUME ["/solr-data"]  
  
# data directory for swiknlp needs special owner to be accessible for solr
user  
RUN mkdir /solr-data-nlp && chown -R 8983:8983 /solr-data-nlp  
  
VOLUME ["/solr-data-nlp"]  
  
# ----------------- #  
# Start #  
# ----------------- #  
USER solr  
EXPOSE 8983  

