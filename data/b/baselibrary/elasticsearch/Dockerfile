FROM baselibrary/java:8  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
## Version  
ENV ELASTICSEARCH_MAJOR 1.7  
ENV ELASTICSEARCH_VERSION 1.7.6  
## Repository  
RUN \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D88E42B4 &&\  
echo "deb http://packages.elastic.co/elasticsearch/1.7 stable main" >
/etc/apt/sources.list.d/elasticsearch.list  
  
## Packages  
RUN \  
apt-get update &&\  
apt-get install -y elasticsearch=$ELASTICSEARCH_VERSION &&\  
rm -rf /var/lib/apt/lists/*  
  
## Environments  
ENV PATH /usr/share/elasticsearch/bin:$PATH  
  
## Scripts  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod a+x /docker-entrypoint.sh  
  
EXPOSE 9200 9300  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
VOLUME ["/usr/share/elasticsearch/data"]  
  
CMD ["elasticsearch"]  

