FROM elasticsearch:2.3.5  
MAINTAINER https://github.com/chocoboxxf/docker-elasticsearch-ik  
  
# add ik files  
ADD container-files/elasticsearch-analysis-ik-1.9.5.zip /tmp/  
  
RUN unzip /tmp/elasticsearch-analysis-ik-1.9.5.zip -d
/usr/share/elasticsearch/plugins/ik  

