FROM rethinkdb:2.3.5  
MAINTAINER Tom Midson <tm@docketbook.io>  
  
ENV CONTAINERBUDDY_VERSION 1.2.1  
COPY rethinkdb-consul.json /etc/rethinkdb-consul.json  
COPY rethinkdb_health.sh /usr/local/bin/rethinkdb_health.sh  
  
USER root  
  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y curl unzip netcat \  
&& curl -L -o containerpilot.tar.gz
https://github.com/joyent/containerpilot/releases/download/2.4.3/containerpilot-2.4.3.tar.gz\  
&& tar -xzf containerpilot.tar.gz -C /usr/local/bin \  
&& rm -r containerpilot.tar.gz \  
&& curl -vo /tmp/consul.zip
https://releases.hashicorp.com/consul/0.7.0/consul_0.7.0_linux_amd64.zip \  
&& unzip /tmp/consul -d /usr/local/bin \  
&& mkdir /config \  
&& mkdir /consul-data  
  
ENV CONTAINERPILOT=file:///etc/rethinkdb-consul.json  
  
EXPOSE 29015 28015 8080  
ENTRYPOINT [ "/usr/local/bin/containerpilot", "rethinkdb", "--bind","all"]  

