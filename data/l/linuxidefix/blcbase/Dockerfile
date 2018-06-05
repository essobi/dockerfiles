# SOLR EMBEDDED  
FROM openjdk:8-jdk  
  
ENV TZ=Europe/Paris  
  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \  
echo $TZ > /etc/timezone && \  
apt-get update && \  
apt-get install -y lsof && \  
mkdir -p /tmp/solr-5.3.1 && \  
wget http://archive.apache.org/dist/lucene/solr/5.3.1/solr-5.3.1.tgz -O
/tmp/solr-5.3.1.tgz && \  
tar -xzvf /tmp/solr-5.3.1.tgz -C /tmp/solr-5.3.1 && \  
rm -rf /tmp/solr-5.3.1.tgz && \  
wget
https://github.com/glowroot/glowroot/releases/download/v0.10.0/glowroot-0.10.0-dist.zip
-O /tmp/glowroot.zip && \  
unzip /tmp/glowroot.zip -d / && \  
rm -rf /tmp/glowroot.zip && \  
apt-get clean  
  
EXPOSE 4000  

