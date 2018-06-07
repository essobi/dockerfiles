FROM alpine:latest  
MAINTAINER m3adow  
  
RUN apk add --no-cache curl  
RUN export CONSUL_TEMPLATE_VERSION=$(curl -s
https://releases.hashicorp.com/consul-template/ \  
| grep -oE 'href="\/consul-template\/[0-9.]*\/"' | head -1 \  
| sed -e 's/href="\/consul-template\/\\([0-9\\.]*\\)\/"/\1/') \  
&& curl -o consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& curl -s \  
https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_SHA256SUMS \  
| grep linux_amd64 | sha256sum -s -c - \  
&& unzip -d /bin/ consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip \  
&& mkdir /conf \  
&& rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip
/var/cache/apk/*  
  
ENTRYPOINT ["/bin/consul-template"]  

