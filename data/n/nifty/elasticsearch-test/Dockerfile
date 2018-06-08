FROM dockerfile/java  
MAINTAINER Nate West <natescott.west@gmail.com>  
  
# The only different between this and
https://index.docker.io/u/dockerfile/elasticsearch/  
# is elasticsearch is running on non-standard ports so you can run it side by
side  
# with another Elasticsearch instance  
# Install ElasticSearch.  
RUN wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-
key add -  
RUN echo "deb http://packages.elasticsearch.org/elasticsearch/1.0/debian
stable main" >> /etc/apt/sources.list  
RUN apt-get update  
RUN apt-get install -y elasticsearch  
  
# Prevent elasticsearch calling `ulimit`.  
RUN sed -i 's/MAX_OPEN_FILES=/# MAX_OPEN_FILES=/g' /etc/init.d/elasticsearch  
  
# Set up non-default ports  
RUN sed -i 's/# transport.tcp.port: 9300 /transport.tcp.port: 9310/g'
/etc/elasticsearch/elasticsearch.yml  
RUN sed -i 's/# http.port: 9200/http.port: 9210/g'
/etc/elasticsearch/elasticsearch.yml  
  
# Expose ports.  
# - 9210: HTTP  
# - 9310: transport  
EXPOSE 9210  
EXPOSE 9310  
# Define an entry point.  
ENTRYPOINT ["/usr/share/elasticsearch/bin/elasticsearch"]  
CMD ["-f"]  

