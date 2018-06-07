FROM gliderlabs/alpine:3.3  
MAINTAINER Dave Finster <df@docketbook.io>  
  
RUN adduser elasticsearch -D && \  
apk update && \  
apk add openjdk8 bash && \  
cd ~ && \  
wget
https://download.elastic.co/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/2.3.2/elasticsearch-2.3.2.tar.gz
&& \  
tar -zxvf elasticsearch-2.3.2.tar.gz && \  
rm elasticsearch-2.3.2.tar.gz && \  
mv elasticsearch-2.3.2 /elasticsearch && \  
chown -R elasticsearch /elasticsearch  
  
USER elasticsearch  
  
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
EXPOSE 9200 9300  
CMD [ "/elasticsearch/bin/elasticsearch"]

