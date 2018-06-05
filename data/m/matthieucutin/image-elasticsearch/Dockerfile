# Pull base image.  
FROM relateiq/oracle-java8  
  
# Install Elasticsearch.  
RUN \  
cd / && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.7.3.tar.gz
&& \  
tar xvzf elasticsearch-1.7.3.tar.gz && \  
rm -f elasticsearch-1.7.3.tar.gz && \  
mv /elasticsearch-1.7.3 /elasticsearch  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Mount elasticsearch.yml config  
ADD config/elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Define working directory.  
WORKDIR /data  
  
# Install head  
RUN /elasticsearch/bin/plugin -install mobz/elasticsearch-head  
  
# Install Marvel  
RUN /elasticsearch/bin/plugin --install elasticsearch/marvel/latest  
  
# Install mapper-attachement  
RUN /elasticsearch/bin/plugin --install elasticsearch/elasticsearch-mapper-
attachments/2.0.0  
  
# Install BigDesk  
RUN /elasticsearch/bin/plugin --install lukas-vlcek/bigdesk  
  
# Install Inquisitor  
RUN /elasticsearch/bin/plugin --install polyfractal/elasticsearch-inquisitor  
  
# Define default command.  
CMD ["/elasticsearch/bin/elasticsearch"]  
  
# Expose ports.  
# - 9200: HTTP  
# - 9300: transport  
EXPOSE 9200  
EXPOSE 9300  

