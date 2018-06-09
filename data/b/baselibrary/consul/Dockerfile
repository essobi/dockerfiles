FROM baselibrary/baseimage:1.0.0  
MAINTAINER ShawnMa <qsma@thoughtworks.com>  
  
## Version  
ENV CONSUL_MAJOR 0.5  
ENV CONSUL_RELEASE 0.5.2  
## Packages  
RUN set -x \  
&& curl -fSL
"https://releases.hashicorp.com/consul/${CONSUL_RELEASE}/consul_${CONSUL_RELEASE}_linux_amd64.zip"
-o consul.zip \  
&& unzip consul.zip -d /usr/bin/ \  
&& rm consul.zip  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
  
WORKDIR /var/lib/consul  
  
VOLUME ["/var/lib/consul"]  
  
CMD ["consul", "agent", "-bootstrap", "-server", "-data-dir",
"/var/lib/consul"]  
  

