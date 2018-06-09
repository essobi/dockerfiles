FROM ticketfly/java:7  
MAINTAINER Guillaume Carre <guillaume.carre@ticketfly.com>  
  
ENV ELASTICSEARCH_VERSION=0.16.5  
RUN wget
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-$ELASTICSEARCH_VERSION.zip
&&\  
unzip elasticsearch*.zip &&\  
mv elasticsearch-$ELASTICSEARCH_VERSION elasticsearch &&\  
sed -i 's/Xss128k/Xss256k/g' elasticsearch/bin/elasticsearch.in.sh  
  
WORKDIR elasticsearch  
  
ADD elasticsearch.yml config  
  
EXPOSE 9200 9300  
CMD ["bin/elasticsearch", "-f"]  
  

