FROM ubuntu:14.04  
MAINTAINER Sandy Lerman <sandy@presencelearning.com>  
  
  
RUN apt-get update && \  
apt-get install -y vim curl build-essential golang gcc wget supervisor && \  
wget https://github.com/elasticsearch/logstash-forwarder/archive/v0.4.0.tar.gz
-O /tmp/logstash-forwarder.tar.gz && \  
cd /tmp && mkdir /tmp/logstash-forwarder && \  
tar xzf logstash-forwarder.tar.gz -C /tmp/logstash-forwarder --strip-
components=1 && \  
cd logstash-forwarder/ && go build -o logstash-forwarder && \  
mkdir -p /opt/logstash-forwarder/bin && cp /tmp/logstash-forwarder/logstash-
forwarder /opt/logstash-forwarder/bin/ && \  
wget https://github.com/hashicorp/consul-
template/releases/download/v0.7.0/consul-template_0.7.0_linux_amd64.tar.gz -O
/tmp/consul_template.tar.gz && \  
mkdir -p /opt/consul_template && tar xzf /tmp/consul_template.tar.gz -C
/opt/consul_template --strip-components=1 && \  
mkdir /opt/consul_template/conf.d && mkdir /opt/consul_template/templates && \  
apt-get remove -y build-essential golang ruby-dev gcc wget && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/{apt,dpkg,cache,log,gems}/ && \  
rm -rf /tmp/*  
  
COPY etchosts.sh /opt/  
RUN chmod +x /opt/etchosts.sh  
  
RUN mkdir -p /var/log/supervisor  
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY consul_template/conf.d /opt/consul_template/conf.d  
COPY consul_template/templates /opt/consul_template/templates  
  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]

