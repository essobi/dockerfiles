FROM java  
ENV LS_VERSION=2.0.0  
RUN curl -sSL
https://download.elasticsearch.org/logstash/logstash/logstash-${LS_VERSION}.tar.gz
\  
| tar -xzf - -C /opt \  
&& mv /opt/logstash-${LS_VERSION} /opt/logstash  
CMD ["/opt/logstash/bin/logstash", "agent" ,"-f", "/opt/logstash/conf.d"]  

