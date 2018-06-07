FROM dockerfile/java:oracle-java7  
MAINTAINER Ganesh Ravi <ganesh.reddy.22@gmail.com>  
  
ENV ES_PKG_NAME elasticsearch-1.4.0  
# Install ElasticSearch.  
RUN cd / && \  
wget
https://download.elasticsearch.org/elasticsearch/elasticsearch/$ES_PKG_NAME.tar.gz
&& \  
tar xvzf $ES_PKG_NAME.tar.gz && \  
rm -f $ES_PKG_NAME.tar.gz && \  
mv /$ES_PKG_NAME /elasticsearch  
  
# Define mountable directories.  
VOLUME ["/data"]  
  
# Mount elasticsearch.yml config  
ADD elasticsearch.yml /elasticsearch/config/elasticsearch.yml  
  
# Define working directory.  
WORKDIR /data  
  
# Installing MongoDB client, so that replicaset can be initiated  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv 7F0CEB10 && \  
echo 'deb http://downloads-distro.mongodb.org/repo/debian-sysvinit dist 10gen'
| tee /etc/apt/sources.list.d/mongodb.list && \  
apt-get update && \  
apt-get install -y mongodb-org-shell  
  
RUN apt-get -y install curl  
  
# Installing Mongo Connector which will connect MongoDB and Elasticsearch  
RUN apt-get -y install python-pip && \  
pip install mongo-connector  
  
ADD run.sh /usr/local/bin/run.sh  
  
RUN chmod 777 /usr/local/bin/run.sh  
  
CMD ["/bin/bash", "/usr/local/bin/run.sh"]  
  
EXPOSE 9200 9300  

