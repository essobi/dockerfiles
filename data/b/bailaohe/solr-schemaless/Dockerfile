FROM bailaohe/java:7  
MAINTAINER He Bai <bai.he@outlook.com>  
  
RUN curl -SL http://archive.apache.org/dist/lucene/solr/4.10.3/solr-4.10.3.tgz
| tar -xzC /opt  
COPY schema.xml /opt/solr-4.10.3/example/solr/collection1/conf/  
COPY solrconfig.xml /opt/solr-4.10.3/example/solr/collection1/conf/  
COPY text_ik/IKAnalyzer2012FF_u1.jar /opt/solr-4.10.3/contrib/extraction/lib/  
COPY text_ik/IKAnalyzer.cfg.xml
/opt/solr-4.10.3/example/solr/collection1/conf/  
COPY text_ik/stopword.dic /opt/solr-4.10.3/example/solr/collection1/conf/  
  
EXPOSE 8983  
CMD /opt/solr-4.10.3/bin/solr start -f  

