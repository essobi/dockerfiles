FROM centos:centos7  
MAINTAINER The ViaQ Community <community@TBA>  
  
EXPOSE 9200  
EXPOSE 9300  
USER 0  
  
ARG USE_SEARCHGUARD=false  
  
ENV HOME=/opt/app-root/src \  
JAVA_VER=1.8.0 \  
ES_VER=2.4.4 \  
SG_VER=2.4.4.10 \  
SG_SSL_VER=2.4.4.19 \  
ES_CLOUD_K8S_VER=2.4.4 \  
OSE_ES_VER=2.4.4.0 \  
ES_HOME=/usr/share/elasticsearch \  
ES_CONF=/usr/share/elasticsearch/config \  
ES_JAVA_OPTS="-Dmapper.allow_dots_in_name=true" \  
INSTANCE_RAM=8G \  
NODE_QUORUM=1 \  
RECOVER_AFTER_NODES=1 \  
RECOVER_EXPECTED_NODES=1 \  
RECOVER_AFTER_TIME=5m \  
PLUGIN_LOGLEVEL=INFO \  
USE_SEARCHGUARD=${USE_SEARCHGUARD:-false} \  
SG_SETUP_ONLY=true  
  
LABEL io.k8s.description="Elasticsearch container for allowing indexing and
searching of aggregated logs" \  
io.k8s.display-name="Elasticsearch ${ES_VER}" \  
io.openshift.expose-services="9200:https, 9300:https" \  
io.openshift.tags="logging,elk,elasticsearch"  
ADD elasticsearch.repo /etc/yum.repos.d/elasticsearch.repo  
ADD run.sh install.sh ${HOME}/  
ADD *.yml ${ES_CONF}/  
ADD index_templates ${ES_CONF}/index_templates  
ADD sg_init.sh ${HOME}/  
RUN ${HOME}/install.sh  
  
WORKDIR ${HOME}  
USER 1000  
CMD ["sh", "/opt/app-root/src/run.sh"]  

