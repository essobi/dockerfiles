FROM dockerfile/java:oracle-java7  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN wget -O - http://packages.elasticsearch.org/GPG-KEY-elasticsearch | apt-
key add - && \  
echo "deb http://packages.elasticsearch.org/logstash/1.4/debian stable main" |
tee -a /etc/apt/sources.list.d/elasticsearch.list && \  
apt-get update && apt-get install logstash  
  
ADD conf/logstash.conf /etc/logstash/conf.d/logstash.conf  
ADD conf/elasticsearch.yml /etc/logstash/elasticsearch.yml  
  
EXPOSE 5000  
ENV JAVA_OPTS -Djava.io.tmpdir=/var/lib/logstash
-Des.config=/etc/logstash/elasticsearch.yml  
  
ENTRYPOINT ["/opt/logstash/bin/logstash", "-f" ,
"/etc/logstash/conf.d/logstash.conf"]  

