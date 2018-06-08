FROM ubuntu:14.04  
MAINTAINER prameswar <engg.pram1@gmail.com>  
  
ENV VERSION=2.1.2  
RUN apt-get update && \  
apt-get install -y wget software-properties-common && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
RUN wget
https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/deb/elasticsearch/${VERSION}/elasticsearch-${VERSION}.deb
&& \  
dpkg -i elasticsearch-${VERSION}.deb && \  
rm elasticsearch-${VERSION}.deb  
  
COPY elasticsearch.yml /etc/elasticsearch/elasticsearch.yml  
COPY start.sh /start.sh  
  
EXPOSE 9200 9300  
RUN chmod +x /start.sh  
  
ENTRYPOINT ["/start.sh"]  
  

