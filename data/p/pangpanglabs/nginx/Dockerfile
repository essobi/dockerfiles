FROM nginx:alpine  
MAINTAINER pangpanglab <pangpanglab@p2shop.cn>  
  
ENV CONSUL_TEMPLATE_VERSION 0.18.1  
ENV CONSUL_TEMPLATE_SHA256
99dcee0ea187c74d762c5f8f6ceaa3825e1e1d4df6c0b0b5b38f9bcb0c80e5c8  
  
# install consul-template  
RUN apk --no-cache add curl ca-certificates \  
&& curl -sSL https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -o /tmp/consul-
template.zip \  
&& echo "${CONSUL_TEMPLATE_SHA256} /tmp/consul-template.zip" > /tmp/consul-
template.sha256 \  
&& sha256sum -c /tmp/consul-template.sha256 \  
&& cd /usr/bin \  
&& unzip /tmp/consul-template.zip \  
&& chmod a+x consul-template \  
&& rm /tmp/consul-template.zip  

