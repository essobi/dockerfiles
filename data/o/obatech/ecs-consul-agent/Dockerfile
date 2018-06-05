FROM gliderlabs/consul-agent:0.6  
MAINTAINER Akram Hussein <akram@tryoba.com>  
  
ADD consul_client.json /etc/consul/consul.json  
  
ADD docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]

