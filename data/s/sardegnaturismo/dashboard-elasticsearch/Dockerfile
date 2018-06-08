FROM ubuntu:14.04  
ENV ES_VERSION 1.7.1  
#Install Updates, Dependencies and Oracle JDK 7  
RUN apt-get update; apt-get install zip netcat -y; \  
apt-get install wget unzip vim python-software-properties software-properties-
common -y; \  
echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
rm -rf /var/cache/oracle-jdk7-installer  
  
# Apply JAVA_HOME  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
  
#Install Elastic Search  
RUN /usr/bin/wget -qO /tmp/es.tgz
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-${ES_VERSION}.tar.gz
&& \  
cd /usr/share && \  
tar xf /tmp/es.tgz && \  
rm /tmp/es.tgz  
  
ENV ES_HOME /usr/share/elasticsearch-${ES_VERSION}  
RUN useradd -d $ES_HOME -M -r elasticsearch && \  
chown -R elasticsearch: $ES_HOME  
  
RUN mkdir /data /conf /backup && touch /data/.CREATED /conf/.CREATED
/backup/.CREATED && chown -R elasticsearch: /data /conf /backup  
# Predispongo la cartella backup in caso di backup/restore  
VOLUME ["/data","/conf"]  
  
ADD ./start /start  
RUN chmod +x /start  
  
WORKDIR $ES_HOME  
USER elasticsearch  
  
RUN echo "path.repo: ["/backup"]" >> $ES_HOME/config/elasticsearch.yml  
  
EXPOSE 9200 9300  
ENV OPTS=-Dnetwork.host=_non_loopback_  
  
CMD ["/start"]  

