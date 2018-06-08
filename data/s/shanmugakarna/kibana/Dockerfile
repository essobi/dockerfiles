FROM ubuntu:15.10  
MAINTAINER Shan <shanmugs_karna@yahoo.com>  
  
#Oracle Java 8  
RUN apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y python-software-properties software-properties-common
wget&& \  
add-apt-repository -y ppa:webupd8team/java && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
/usr/bin/debconf-set-selections && \  
apt-get update && apt-get install -y oracle-java8-installer && \  
apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
RUN mkdir -p /opt/kibana && \  
wget -qO-
https://download.elastic.co/kibana/kibana/kibana-4.1.2-linux-x64.tar.gz | tar
-xzf - -C /opt/kibana --strip-components=1  
  
WORKDIR /opt/kibana  
  
RUN sed -i '2i\sed -i
"s/ELASTICSEARCH_HOST/$ELASTICSEARCH_HOST/g;s/ELASTICSEARCH_PORT/$ELASTICSEARCH_PORT/g"
./config/kibana.yml\' ./bin/kibana && sed -i
's/localhost:9200/ELASTICSEARCH_HOST:ELASTICSEARCH_PORT/g' ./config/kibana.yml  
  
ENV ELASRICSEARCH_HOST=localhost  
ENV ELASTICSEARCH_PORT=9200  
CMD ./bin/kibana  

