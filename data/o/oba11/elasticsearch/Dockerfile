FROM ubuntu:trusty  
MAINTAINER Oluwaseun Obajobi <oba@obajobi.com>  
  
# Need to update the package repo first  
RUN apt-get -qq update  
  
# Install Required Packages  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -qq adduser \  
openjdk-7-jre-headless  
  
# Download Elasticsearch Package  
ADD
https://download.elasticsearch.org/elasticsearch/elasticsearch/elasticsearch-1.4.4.deb
/tmp/elasticsearch.deb  
  
# Install the Elasticsearch Package  
RUN dpkg -i /tmp/elasticsearch.deb  
  
# Set the clustername and Mountpoint  
RUN sed -i 's/^\\(\\#cluster.name: elasticsearch\\)$/\1\ncluster.name:
elasticsearch/' /etc/elasticsearch/elasticsearch.yml && \  
sed -i 's/^\\(\\#path.data: \/path\/to\/data\\)$/\1\npath.data: \/data/'
/etc/elasticsearch/elasticsearch.yml && \  
sed -i -e '$a\script.disable_dynamic: true'
/etc/elasticsearch/elasticsearch.yml && \  
sed -i 's/^\\(\\#MAX_OPEN_FILES=.\\+\\)$/\1\nMAX_OPEN_FILES=65535/'
/etc/default/elasticsearch  
  
# Clean Up packages  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
find /var/log -type f | while read f; do echo -ne '' > $f; done;  
  
# Exposed Volumes  
VOLUME ["/data"]  
  
# Expose ports  
EXPOSE 9200 9300  
CMD ["/usr/share/elasticsearch/bin/elasticsearch"]  

