FROM mycrypt/debian-java  
MAINTAINER Bai Xiaoyong lostitle@gmail.com  
  
RUN mkdir /opt/elasticsearch  
RUN wget -qO-
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.2.2.tar.gz
\  
| tar zxvf - -C /opt/elasticsearch --strip 1  
  
ENV PATH /opt/elasticsearch/bin:$PATH  
  
EXPOSE 9200 9300  

