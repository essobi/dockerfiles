FROM shurshun/alpine-moscow  
  
LABEL author "Korviakov Andrey"  
LABEL maintainer "4lifenet@gmail.com"  
  
RUN \  
CONSUL_VERSION=$(curl -s https://api.github.com/repos/hashicorp/consul/tags |
jq -r ".[0] .name" | tr -d v) \  
&& curl -fSl
https://releases.hashicorp.com/consul/${CONSUL_VERSION}/consul_${CONSUL_VERSION}_linux_amd64.zip
-o /tmp/consul.zip \  
&& unzip /tmp/consul.zip -d /bin \  
&& rm -f /tmp/consul.zip  
  
RUN \  
NET_ALIASES_VERSION=$(curl -s https://api.github.com/repos/shurshun/net-
aliases/tags | jq -r ".[0] .name") \  
&& curl -fSlL https://github.com/shurshun/net-
aliases/releases/download/${NET_ALIASES_VERSION}/net-
aliases_${NET_ALIASES_VERSION}_linux_amd64.tar.gz | tar -C /bin -zx  
  
ENTRYPOINT ["consul", "watch", "-type", "key", "-key", "node/$HOSTNAME/ips",
"/bin/net-aliases"]

