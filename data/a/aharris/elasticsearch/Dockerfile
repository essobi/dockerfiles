# Elasticsearch  
# docker pull barnybug/elasticsearch  
FROM barnybug/openjdk-7-jre  
MAINTAINER Austin Harris <austin.w.harris+docker@gmail.com>  
  
ENV ES_VERSION 1.4.1  
# install wget  
RUN apt-get install -y wget && apt-get clean  
  
# download and unpack elasticsearch  
RUN wget -q
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-$ES_VERSION.tar.gz
-O - | tar zxvf - && \  
mv /elasticsearch-$ES_VERSION /elasticsearch  
  
# install the kopf plugin  
RUN /elasticsearch/bin/plugin -install lmenezes/elasticsearch-kopf  
  
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
VOLUME ["/data", "/logs"]  
  
EXPOSE 9200 9300  
CMD ["elasticsearch/bin/elasticsearch"]  

