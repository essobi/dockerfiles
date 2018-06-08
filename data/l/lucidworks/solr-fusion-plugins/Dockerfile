  
FROM makuk66/docker-solr:5.2.1  
MAINTAINER Kiran Chitturi "kiran.chitturi@lucidworks.com"  
  
ENV SOLR_USER solr  
  
# Using IP address instead of download.lucidworks.com because docker is not
able to resolve the dns name on local machine with boot2docker  
RUN cd /opt/solr && \  
curl -LO http://download.lucidworks.com/lw-fusion-solr-plugins-
jars/solr-5.2.1-plugins-for-fusion-0.2.jar && \  
mkdir -p /opt/solr/server/solr/configsets/modified_techproducts_configs && \  
cp -r /opt/solr/server/solr/configsets/sample_techproducts_configs/conf
/opt/solr/server/solr/configsets/modified_techproducts_configs/  
  
COPY solrconfig.xml
/opt/solr/server/solr/configsets/modified_techproducts_configs/conf/  
  
RUN /opt/solr/bin/solr start && \  
sleep 10 && \  
/opt/solr/bin/solr create_core -c collection1 -d
/opt/solr/server/solr/configsets/modified_techproducts_configs/conf && \  
/opt/solr/bin/post -c collection1 example/exampledocs/*.xml && \  
/opt/solr/bin/solr stop -all  
  
CMD ["/bin/bash", "-c", "/opt/solr/bin/solr -f"]  

