FROM docker.io/elasticsearch:latest  
MAINTAINER Zephyre <haizi.zh@gmail.com>  
  
# Install marvel  
RUN plugin -i elasticsearch/marvel/latest  
  
# Install IKAnalyzer  
COPY elasticsearch-analysis-ik-1.4.0.zip /tmp/  
RUN plugin -i analysis-ik --url file:///tmp/elasticsearch-analysis-
ik-1.4.0.zip && rm -rf /tmp/elasticsearch-analysis-ik-1.4.0.zip  
RUN mkdir -p /usr/share/elasticsearch/plugins/analysis-ik/_site  
  
# Add configuration files  
ADD config /usr/share/elasticsearch/config  

