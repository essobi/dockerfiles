FROM alpine:3.5  
  
ENV CONSUL_VERSION=0.9.3  
ENV HIERA_EYAML_VERSION=2.1.0  
  
RUN apk add --no-cache --update ruby curl && \  
gem install --no-ri --no-rdoc hiera-eyaml -v ${HIERA_EYAML_VERSION} && \  
curl -L
https://releases.hashicorp.com/consul/0.9.3/consul_0.9.3_linux_amd64.zip >
/tmp/consul.zip && \  
unzip -d /usr/bin/ /tmp/consul.zip && \  
rm -f /tmp/consul.zip  

