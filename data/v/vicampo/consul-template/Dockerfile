FROM alpine:3.5  
LABEL maintainer "devops@vicampo.de"  
  
ENV CONSUL_TEMPLATE_VERSION=0.18.3  
RUN apk --update add haproxy wget bash curl  
RUN ( wget --no-check-certificate https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -O
/tmp/consul_template.zip && unzip /tmp/consul_template.zip && mv consul-
template /usr/bin && rm -rf /tmp/* )  
  
COPY src/etc/haproxy/haproxy.cfg /etc/haproxy/haproxy.cfg  
COPY src/etc/consul-template.json /etc/consul-template.json  
COPY src/templates/ /templates  
VOLUME ["/templates"]  
  
EXPOSE 8080  

