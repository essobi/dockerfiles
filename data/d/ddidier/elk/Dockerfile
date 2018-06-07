#  
# ddidier/elk  
#  
# docker build -t ddidier/elk .  
FROM sebp/elk:es233_l232_k451  
MAINTAINER David DIDIER  
  
ENV ES_HOME /usr/share/elasticsearch  
ENV KB_HOME /opt/kibana  
ENV LS_HOME /opt/logstash  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y --no-install-recommends gawk jq wget && \  
apt-get autoremove -y && \  
rm -rf /var/cache/* && \  
rm -rf /var/lib/apt/lists/* && \  
gosu elasticsearch ${ES_HOME}/bin/plugin install license && \  
gosu elasticsearch ${ES_HOME}/bin/plugin install marvel-agent && \  
gosu logstash ${LS_HOME}/bin/logstash-plugin install logstash-filter-translate
&& \  
gosu kibana ${KB_HOME}/bin/kibana plugin --install elastic/sense && \  
gosu kibana ${KB_HOME}/bin/kibana plugin --install elasticsearch/marvel  
  
VOLUME ["/etc/logstash", "/var/tmp/logs"]  

