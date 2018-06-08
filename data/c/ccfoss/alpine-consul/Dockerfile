FROM alpine:edge  
MAINTAINER Chaitanya Akkineni <cakkinen@cisco.com>  
  
RUN echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories && \  
apk add --update confd@testing bash unzip net-tools netcat-openbsd openssl &&
\  
rm -rf /var/cache/apk/*  
  
RUN wget -O consul-template.zip \  
https://releases.hashicorp.com/consul-template/0.16.0/consul-
template_0.16.0_linux_amd64.zip && \  
unzip consul-template.zip -d /usr/local/bin && \  
chmod +x /usr/local/bin/consul-template && \  
wget -O consul.zip \  
https://releases.hashicorp.com/consul/0.7.0/consul_0.7.0_linux_amd64.zip && \  
unzip consul.zip -d /usr/local/bin && \  
chmod +x /usr/local/bin/consul && \  
mkdir -p /etc/consul.d/ && \  
rm -rf consul-template.zip  
  
ADD entrypoint.sh /usr/local/bin  
RUN chmod +x /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  

