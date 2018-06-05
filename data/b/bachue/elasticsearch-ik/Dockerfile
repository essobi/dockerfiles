FROM docker.elastic.co/elasticsearch/elasticsearch:6.2.4  
MAINTAINER Rong Zhou "zhourong@qiniu.com"  
  
RUN wget -c --tries=0 -O /tmp/elasticsearch-analysis-ik.zip
https://github.com/medcl/elasticsearch-analysis-
ik/releases/download/v6.2.4/elasticsearch-analysis-ik-6.2.4.zip && \  
unzip /tmp/elasticsearch-analysis-ik.zip -d /usr/share/elasticsearch/plugins
&& \  
rm -rf /tmp/elasticsearch-analysis-ik.zip  

