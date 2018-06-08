FROM java:7-jre  
  
RUN cd /tmp && \  
wget
https://download.elasticsearch.org/logstash/logstash/logstash-1.4.2.tar.gz &&
\  
tar -xzvf ./logstash-1.4.2.tar.gz && \  
mv ./logstash-1.4.2 /opt/logstash && \  
rm ./logstash-1.4.2.tar.gz && \  
/opt/logstash/bin/plugin install contrib && \  
echo "GMT [Gg][Mm][Tt]" >> /opt/logstash/patterns/grok-patterns && \  
echo "DATESTAMP %{DAY}, %{MONTHDAY} %{MONTH} %{YEAR} %{TIME}" >>
/opt/logstash/patterns/grok-patterns && \  
echo "DATESTAMP_GMT %{DATESTAMP} %{GMT}" >> /opt/logstash/patterns/grok-
patterns  
  
ADD container.conf /opt/logstash/container.conf  
CMD /opt/logstash/bin/logstash agent -f /opt/logstash/container.conf -l
/var/log/logstash.log  

