##  
#  
# Dockerfile for Elastic v 1.6.0  
#  
##  
FROM sunnybhanot/java  
  
# Version  
ENV ES_VERSION 1.7.0  
# Install  
RUN cd / \  
&& wget
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-$ES_VERSION.tar.gz
\  
&& tar xzf elasticsearch-$ES_VERSION.tar.gz \  
&& rm -f elasticsearch-$ES_VERSION.tar.gz \  
&& mv /elasticsearch-$ES_VERSION /elastic \  
&& /elastic/bin/plugin -install mobz/elasticsearch-head \  
&& /elastic/bin/plugin -install royrusso/elasticsearch-HQ  
  
# Mount dir  
VOLUME ["/data"]  
  
# Mount config  
ADD config/elasticsearch.yml /elastic/config/elasticsearch.yml  
  
# Working Directory  
WORKDIR /data  
  
# Default Command  
CMD ["/elastic/bin/elasticsearch"]  
  
# Expose Ports  
EXPOSE 9200  
EXPOSE 9300  

