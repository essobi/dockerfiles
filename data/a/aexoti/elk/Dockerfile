FROM aexoti/jre:8  
  
ENV RETENTION=30  
ENV TIME_UNIT=days  
  
RUN apk add --update wget ca-certificates supervisor nodejs bash && \  
cd /opt && \  
wget
https://download.elastic.co/elasticsearch/elasticsearch/elasticsearch-1.7.2.tar.gz
-O /opt/elastic.tar.gz && \  
tar -zxvf elastic.tar.gz && \  
mkdir /opt/elastic && \  
mv /opt/elasticsearch-1.7.2/lib /opt/elastic/lib && \  
mv /opt/elasticsearch-1.7.2/config /opt/elastic/config && \  
mv /opt/elasticsearch-1.7.2/bin /opt/elastic/bin && \  
rm /opt/elasticsearch-1.7.2 -rf && \  
rm elastic.tar.gz && \  
mkdir /etc/supervisor.d/ && \  
printf "[supervisord]\nnodaemon=true\n\n[include]\nfiles =
/etc/supervisor.d/*.conf\n" > /etc/supervisord.conf && \  
printf "[program:elasticsearch]\ncommand=/opt/elastic/bin/elasticsearch\n
autorestart=true\n" >/etc/supervisor.d/elasticsearch.conf && \  
wget
https://download.elasticsearch.org/kibana/kibana/kibana-4.0.1-linux-x64.tar.gz
-O /opt/kibana.tar.gz && \  
tar -zxvf /opt/kibana.tar.gz && \  
mv kibana-4.0.1-linux-x64 kibana && \  
rm kibana.tar.gz && \  
printf "[program:kibana]\ncommand=/opt/kibana/bin/kibana\n autorestart=true\n"
>/etc/supervisor.d/kibana.conf && \  
wget https://download.elastic.co/logstash/logstash/logstash-1.5.4.tar.gz -O
/opt/logstash.tar.gz && \  
tar -zxvf /opt/logstash.tar.gz && \  
mv logstash-1.5.4 logstash && \  
rm logstash.tar.gz && \  
echo $'input { \n\  
tcp {\n\  
port => 5000\n\  
type => syslog\n\  
}\n\  
udp {\n\  
port => 5000\n\  
type => syslog\n\  
}\n\  
}\n\  
filter {\n\  
if [type] == "syslog" {\n\  
grok {\n\  
match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp}
%{SYSLOGHOST:syslog_hostname}
%{DATA:syslog_program}(?:\[%{POSINT:syslog_pid}\])?:
%{GREEDYDATA:syslog_message}" }\n\  
add_field => [ "received_at", "%{@timestamp}" ]\n\  
add_field => [ "received_from", "%{host}" ]\n\  
}\n\  
syslog_pri { }\n\  
date {\n\  
match => [ "syslog_timestamp", "MMM d HH:mm:ss", "MMM dd HH:mm:ss" ]\n\  
}\n\  
}\n\  
}\n\  
output {\n\  
elasticsearch { host => localhost }\n\  
}\n'\  
> /opt/logstash/logstash.conf && \  
printf "[program:logstash]\ncommand=/opt/logstash/bin/logstash -f
/opt/logstash/logstash.conf \nautorestart=true\n" >
/etc/supervisor.d/logstash.conf && \  
  
wget https://bootstrap.pypa.io/get-pip.py -O /opt/get-pip.py && \  
python /opt/get-pip.py && \  
rm /opt/get-pip.py && \  
pip install elasticsearch-curator && \  
echo $'[program:curator]\ncommand=/bin/bash -c \"while true; do curator --host
localhost delete indices --older-than $RETENTION --time-unit $TIME_UNIT
--timestring \'%%Y.%%m.%%d\' &>/dev/null; sleep 3; done\"\nautorestart=true' >
/etc/supervisor.d/curator.conf && \  
  
rm /var/cache/apk/*  
  
CMD ["supervisord"]  
  
  
  

