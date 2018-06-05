FROM alpine  
  
MAINTAINER Andrey Popelo andrey@popelo.com  
  
RUN apk add \--update git go && \  
mkdir /opt && \  
git clone git://github.com/elasticsearch/logstash-forwarder.git /opt/logstash-
forwarder && \  
cd /opt/logstash-forwarder && \  
go build && \  
rm -rf /opt/logstash-forwarder/.git && \  
apk del -r git go  
  
ENTRYPOINT ["/opt/logstash-forwarder/logstash-forwarder"]  
CMD ["-config", "/etc/logstash-forwarder/config.json"]  

