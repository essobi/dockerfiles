FROM centos:centos7  
MAINTAINER Marcin Ryzycki marcin@m12.io, Przemyslaw Ozgo linux@ozgo.info  
  
RUN \  
yum update -y && \  
yum install -y golang git wget tar && \  
mkdir -p /opt/logstash/ssl && \  
mkdir -p /opt/logstash-forwarder && \  
wget https://github.com/elasticsearch/logstash-forwarder/archive/v0.4.0.tar.gz
&& \  
tar zxvf v0.4.0.tar.gz -C /opt/logstash-forwarder --strip-components=1 && \  
cd /opt/logstash-forwarder/ && \  
go build && \  
yum remove -y tar wget git golang && \  
yum clean all  
  
ENV LOGSTASH_IP 127.0.0.1  
  
COPY container-files /  
  
CMD /start.sh  

