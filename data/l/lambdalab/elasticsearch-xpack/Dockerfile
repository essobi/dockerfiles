FROM quay.io/pires/docker-elasticsearch-kubernetes:5.4.0  
RUN echo y | NODE_NAME=dummy /elasticsearch/bin/elasticsearch-plugin install
x-pack  
  
RUN echo "xpack.security.enabled: false" >>
/elasticsearch/config/elasticsearch.yml  
RUN echo "xpack.ml.enabled: false" >> /elasticsearch/config/elasticsearch.yml  
RUN rm -rf /elasticsearch/plugins/x-pack/platform/linux-x86_64

