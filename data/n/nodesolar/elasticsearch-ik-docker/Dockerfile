FROM centos:latest  
MAINTAINER feiin(https://github.com/feiin/elasticsearch-ik-docker)  
  
RUN yum -y install java-1.8.0-openjdk && yum -y install unzip  
  
ENV ES_VERSION 2.3.2  
RUN curl -O
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/zip/elasticsearch/${ES_VERSION}/elasticsearch-${ES_VERSION}.zip
&& \  
unzip elasticsearch-${ES_VERSION}.zip && \  
mv elasticsearch-${ES_VERSION} /elasticsearch && \  
rm -f elasticsearch-${ES_VERSION}.zip  
  
ENV ES_IK_VERSION 1.9.2  
RUN curl -o elasticsearch-analysis-ik-${ES_IK_VERSION}.zip -L -e '; auto'
https://github.com/medcl/elasticsearch-analysis-
ik/releases/download/v${ES_IK_VERSION}/elasticsearch-analysis-
ik-${ES_IK_VERSION}.zip && \  
mkdir -p /elasticsearch/plugins/ik/ && \  
unzip elasticsearch-analysis-ik-${ES_IK_VERSION}.zip -d
/elasticsearch/plugins/ik/ && \  
rm -f elasticsearch-analysis-ik-${ES_IK_VERSION}.zip  
  
RUN mkdir -p /elasticsearch/plugins/ik/ && \  
useradd elasticsearch && \  
chown -R elasticsearch:elasticsearch /elasticsearch  
  
COPY run.sh /  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200 9300  
CMD ["/bin/bash", "/run.sh"]  
  

