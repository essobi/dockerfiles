FROM openjdk:8  
ENV SOLR_VER="7.1.0" SOLR_DEST="/solrdata"  
ENV INSTANCEDIR="${SOLR_DEST}/solr/rcloudnotebooks"  
# Install solr  
#ADD solr-${SOLR_VER}.tgz /  
RUN curl -L
http://archive.apache.org/dist/lucene/solr/${SOLR_VER}/solr-${SOLR_VER}.tgz |
tar xz  
  
ADD conf ${INSTANCEDIR}/conf/  
ADD solrsetup.sh /  
  
# Copy in the setup files and fix permissions  
RUN useradd docker \  
&& ln -s -f /solr-${SOLR_VER} /solr \  
&& mkdir -p ${INSTANCEDIR}/data \  
&& chown -R docker ${SOLR_DEST} \  
&& chmod -R 644 ${SOLR_DEST} \  
&& chmod 755 /solrsetup.sh  
  
EXPOSE 8983  
ENTRYPOINT /solrsetup.sh  

