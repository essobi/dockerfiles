FROM zooniverse/java  
  
ADD logstash.list /etc/apt/sources.list.d/logstash.list  
ADD start_logstash.sh /  
ADD http://packages.elasticsearch.org/GPG-KEY-elasticsearch /GPG-KEY-
elasticsearch  
  
RUN apt-key add /GPG-KEY-elasticsearch && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \  
DEBIAN_FRONTEND=noninteractive apt-get -y -q install logstash logstash-contrib  
  
ENTRYPOINT /start_logstash.sh  

