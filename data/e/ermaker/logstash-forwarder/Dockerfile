FROM golang  
ENV LF_VERSION=0.4.0  
RUN mkdir -p /opt/logstash-forwarder \  
&& curl -sSL https://github.com/elastic/logstash-
forwarder/archive/v${LF_VERSION}.tar.gz \  
| tar -xzf - -C /opt/logstash-forwarder --strip-components=1 \  
&& (cd /opt/logstash-forwarder; go build)  
CMD ["/opt/logstash-forwarder/logstash-forwarder", "-config",
"/opt/conf.d/logstash-forwarder.conf"]  

