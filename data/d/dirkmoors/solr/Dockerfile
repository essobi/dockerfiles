###########################################################  
# Solr  
###########################################################  
FROM debian:jessie  
MAINTAINER Dirk Moors  
  
ENV SOLR_VERSION 4.10.4  
ENV SOLR_ROOT /opt/solr  
ENV SOLR_CONFIG_ROOT /opt/solr/config  
ENV DEPENDENCIES /tmp/dependencies  
  
ADD dependencies ${DEPENDENCIES}  
  
RUN set -x \  
&& buildDeps=`cat ${DEPENDENCIES}/builddeps.txt`\  
&& deps=`cat ${DEPENDENCIES}/deps.txt`\  
&& echo 'deb http://httpredir.debian.org/debian jessie-backports main contrib
non-free' >> /etc/apt/sources.list \  
&& apt-get update \  
&& apt-get install -y ${deps} ${buildDeps} --no-install-recommends \  
&& cd ${HOME} \  
&& curl -O
http://apache.parentingamerica.com/lucene/solr/${SOLR_VERSION}/solr-${SOLR_VERSION}.tgz
\  
&& tar zxf solr-${SOLR_VERSION}.tgz \  
&& rm -rf solr-${SOLR_VERSION}.tgz \  
&& mv ${HOME}/solr-${SOLR_VERSION} ${SOLR_ROOT}/ \  
&& mv ${SOLR_ROOT}/example/ ${SOLR_CONFIG_ROOT}/ \  
&& cd ${SOLR_CONFIG_ROOT} \  
&& rm -rf solr && rm -rf multicore && rm -rf example-* \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge -y --auto-remove $buildDeps  
  
WORKDIR ${SOLR_CONFIG_ROOT}  
  
CMD ["java", "-Dsolr.solr.home=cores", "-jar", "start.jar"]  
  
  

