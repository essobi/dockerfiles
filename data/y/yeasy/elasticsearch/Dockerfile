# This will prepare a elasticsearch with head, bigdesk plugins installed.  
# See http://localhost:9200/_plugin/head/ and
http://localhost:9200/_plugin/bigdesk/ after booted.  
# A logstash_netflow- started index will be parsed according to the
logstash_netflow.json.  
FROM elasticsearch:2.3  
MAINTAINER Baohua Yang  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head \  
&& /usr/share/elasticsearch/bin/plugin install lukas-vlcek/bigdesk \  
&& /usr/share/elasticsearch/bin/plugin install license \  
&& /usr/share/elasticsearch/bin/plugin install -b marvel-agent  
  
COPY ./logstash_netflow.json /tmp/  

