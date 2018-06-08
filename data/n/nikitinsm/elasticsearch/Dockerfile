FROM elasticsearch:5.2.2  
WORKDIR /usr/share/elasticsearch  
  
RUN bin/elasticsearch-plugin install
http://dl.bintray.com/content/imotov/elasticsearch-
plugins/org/elasticsearch/elasticsearch-analysis-
morphology/5.2.2/elasticsearch-analysis-morphology-5.2.2.zip  
  
COPY ./config/elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  

