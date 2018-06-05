FROM million12/centos-supervisor  
MAINTAINER Przemyslaw Ozgo <linux@ozgo.info>  
  
ADD forwarder.conf /etc/forwarder/forwarder.conf  
ADD env.sh /config/init/env.sh  
  
ENV LOGSTASH_IP 127.0.0.1  
RUN \  
yum update -y && \  
yum install -y golang git && \  
yum clean all && \  
mkdir -p /opt/logstash/ssl && \  
cd /opt && \  
git clone git://github.com/elasticsearch/logstash-forwarder.git && \  
cd /opt/logstash-forwarder/ && \  
git checkout ISSUE-221 && \  
go build  
  
ADD supervisord.conf /etc/supervisor.d/logstash-forwarder.conf  
  
VOLUME [ "/etc/forwarder", "/opt/logstash/ssl", "/data/log" ]  

