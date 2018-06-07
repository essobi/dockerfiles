FROM docker.elastic.co/elasticsearch/elasticsearch:6.2.4  
#update jdk to solve CVE  
RUN yum install -y java-1.8.0-openjdk-headless  
  
COPY plugins/readonlyrest-1.16.19_es6.2.4.zip /tmp/  
  
  
RUN /usr/share/elasticsearch/bin/elasticsearch-plugin remove x-pack \  
&& /usr/share/elasticsearch/bin/elasticsearch-plugin install analysis-icu  
  
  
  
RUN mv /usr/local/bin/docker-entrypoint.sh /usr/local/bin/elastic-
entrypoint.sh  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
  
COPY config /usr/share/elasticsearch/config  
  
RUN mv /usr/share/elasticsearch/config/readonlyrest.yml /tmp  
  

