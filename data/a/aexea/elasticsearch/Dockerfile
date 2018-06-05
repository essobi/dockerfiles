FROM elasticsearch:1.5  
MAINTAINER Aexea Carpentry  
  
ADD elasticsearch.yml /usr/share/elasticsearch/config/elasticsearch.yml  
RUN plugin install elasticsearch/elasticsearch-cloud-aws/2.6.0  
RUN plugin install org.codelibs/elasticsearch-dataformat/1.6.0  
RUN plugin install csv -url
http://xbib.org/repository/org/xbib/elasticsearch/plugin/elasticsearch-
csv/1.7.2.0/elasticsearch-csv-1.7.2.0-plugin.zip  

