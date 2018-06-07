FROM java:8  
ENV VERSION 6.6.2  
ENV SOLR_PID_DIR="/var/solr"  
ENV SOLR_HOME="/var/solr/data"  
ENV LOG4J_PROPS="/var/solr/log4j.properties"  
ENV SOLR_LOGS_DIR="/var/solr/logs"  
ENV SOLR_PORT="8983"  
ENV HOME="/home/solr"  
RUN groupadd solr && useradd -g solr solr && mkdir /home/solr && chown
solr:solr /home/solr && mkdir -p /var/solr/data && chown solr:solr
/var/solr/data && \  
apt update && apt install -y wget unzip sudo && \  
cd /opt && wget
http://archive.apache.org/dist/lucene/solr/$VERSION/solr-$VERSION.zip && unzip
*.zip && \  
cd solr-*/bin/ && ./install_solr_service.sh ../../solr-$VERSION.zip -i /opt -d
/var/solr -u solr -s solr -p 8983 -n && chown solr:solr /home/solr && mkdir -p
/opt/data && cp -R /var/solr/data/* /opt/data/  
  
ADD schema.xml /opt  
ADD solrconfig.xml /opt  
  
ADD start.sh /opt/solr/bin  
  
WORKDIR /opt/solr/bin  
  
EXPOSE 8983  
VOLUME /var/solr/data  
  
CMD ./start.sh  
  

