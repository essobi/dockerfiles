FROM concretesolutions/ubuntu-dev  
  
# Install solr  
RUN apt-get update &&\  
apt-get -y install mysql-server &&\  
apt-get clean && rm -rf /var/lib/apt/lists/* &&\  
mkdir -p /opt &&\  
cd /opt && wget http://archive.apache.org/dist/lucene/solr/3.5.0/apache-
solr-3.5.0.tgz &&\  
tar -C /opt --extract --file /opt/apache-solr-3.5.0.tgz  
  
# Expose solr port  
EXPOSE 8983  
# Execute solr as default container command  
CMD ["/bin/bash", "-c", "cd /opt/apache-solr-3.5.0/example; java -jar
start.jar"]

