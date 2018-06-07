FROM centos:7  
MAINTAINER Horatiu Eugen Vlad <info@vlad.eu>  
  
RUN yum install -y epel-release && \  
yum -y install java-1.8.0-openjdk.x86_64 nss_wrapper && \  
yum clean all  
  
ENV USER elasticsearch  
ENV HOME /usr/share/elasticsearch  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
ENV ES_USER=${USER} \  
ES_GROUP=root \  
ES_HOME=${HOME} \  
CONF_DIR=/etc/elasticsearch \  
DATA_DIR=/var/lib/elasticsearch \  
LOG_DIR=/var/log/elasticsearch \  
SCRIPTS_DIR=/etc/elasticsearch/scripts  
  
COPY elasticsearch.repo /etc/yum.repos.d/elasticserach.repo  
ENV ELASTICSEARCH_VERSION 5.3.0-1  
RUN yum -y install elasticsearch-${ELASTICSEARCH_VERSION}.noarch && \  
yum clean all  
  
COPY passwd.in ${HOME}/  
COPY config ${CONF_DIR}  
COPY entrypoint /  
RUN for path in ${CONF_DIR} ${DATA_DIR} ${LOG_DIR} ${SCRIPTS_DIR}; do \  
mkdir -p "$path" && chmod -R ug+rwX "$path" && chown -R ${ES_USER}:${ES_GROUP}
"$path"; \  
done  
  
EXPOSE 9200 9300  
USER 1000  
  
ENTRYPOINT ["/entrypoint"]  
CMD ["elasticsearch", "-Edefault.path.conf=/etc/elasticsearch"]  

