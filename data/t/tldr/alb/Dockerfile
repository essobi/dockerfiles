# 3.2 is the latest one with haproxy 1.5.x; unfortunately 1.6 changes the
config file format  
# so the consul templates need to be updated, we'll pin to 3.2 for now  
FROM alpine:3.2  
MAINTAINER TLDR  
  
ENV CONSUL_TEMPLATE_VERSION=0.13.0  
# Updata wget to get support for SSL  
RUN apk --update add haproxy wget  
  
# Download consul-template  
RUN ( wget --no-check-certificate https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -O
/tmp/consul_template.zip && unzip /tmp/consul_template.zip && mv consul-
template /usr/bin && rm -rf /tmp/* )  
  
COPY files/haproxy.json /haproxy.json  
COPY files/haproxy.ctmpl /haproxy.ctmpl  
  
ENTRYPOINT ["consul-template","-config=/haproxy.json"]  
CMD ["-consul=consul.service.consul:8500"]  

