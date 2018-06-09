FROM ubuntu:14.04  
MAINTAINER tech@texastribune.org  
  
RUN apt-get update  
  
# set up to recognize repo  
RUN apt-get install -y wget  
RUN wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-
key add -  
RUN echo "deb http://packages.elasticsearch.org/elasticsearch/1.3/debian
stable main" > /etc/apt/sources.list.d/elasticsearch.list  
RUN apt-get update -y  
  
# requires java  
RUN apt-get install -y openjdk-7-jre-headless  
RUN apt-get install elasticsearch  
  
# optional:  
RUN /usr/share/elasticsearch/bin/plugin -install lmenezes/elasticsearch-kopf  
  
CMD ["/usr/share/elasticsearch/bin/elasticsearch"]  
  
EXPOSE 9200  
EXPOSE 9300  

