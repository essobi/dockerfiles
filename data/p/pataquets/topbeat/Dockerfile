FROM pataquets/ubuntu:xenial  
  
RUN \  
apt-key adv --keyserver hkp://hkps.pool.sks-keyservers.net --recv-keys
D88E42B4 && \  
echo "deb https://packages.elastic.co/beats/apt stable main" >
/etc/apt/sources.list.d/beats.list  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y topbeat \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
sed -i 's/localhost:9200/elasticsearch:9200/' /etc/topbeat/topbeat.yml && \  
sed -i 's/localhost:5044/logstash:5044/' /etc/topbeat/topbeat.yml  
  
ENTRYPOINT [ "topbeat", "-e" ]  

