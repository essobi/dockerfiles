# influenced by: errordeveloper/weave-elasticsearch-minimal  
# TODO: should probably move to something a tad bit more supported  
FROM errordeveloper/oracle-jre  
# FROM jeanblanchard/busybox-java:8 -- gunzip fails  
MAINTAINER Adam Greene <adam.greene@gmail.com>  
  
ENV ELASTICSEARCH_BINARY_RELEASE 1.4.2  
RUN curl \  
\--silent \  
\--location \  
\--retry 3 \  
\--cacert /etc/ssl/certs/Go_Daddy_Class_2_CA.crt \  
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-$ELASTICSEARCH_BINARY_RELEASE.tar.gz
\  
| gunzip \  
| tar x -C /usr/ \  
&& ln -s /usr/elasticsearch-$ELASTICSEARCH_BINARY_RELEASE /usr/elasticsearch  
  
# need to run as root as long as dockerfile/elasticsearch created all the dirs
under root  
# RUN useradd -Mr elasticsearch  
# USER elasticsearch  
ADD elasticsearch.conf /usr/elasticsearch/config/elasticsearch.yml  
  
# Install plugins  
RUN /usr/elasticsearch/bin/plugin -s --install elasticsearch/marvel/latest  
  
VOLUME [ "/data" ]  
EXPOSE 9200  
EXPOSE 9300  
ENTRYPOINT [ "/usr/elasticsearch/bin/elasticsearch" ]

