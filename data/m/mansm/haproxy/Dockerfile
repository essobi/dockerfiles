FROM debian:latest  
MAINTAINER Mans Matulewicz  
ENV CONSUL_TEMPLATE_VERSION=0.12.2  
RUN apt-get update && apt-get install -y haproxy wget unzip && apt-get clean  
RUN ( wget --no-check-certificate https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip -O
/tmp/consul_template.zip && unzip /tmp/consul_template.zip && mv consul-
template /usr/bin && rm -rf /tmp/* )  
  
COPY haproxy.ctmpl /etc/haproxy.ctmpl  
COPY haproxy.json /etc/haproxy.json  
  
EXPOSE 80/tcp 9000/tcp  
CMD ["consul-template", "-config=/etc/haproxy.json",
"-consul=consul.service.dc1.consul:8500"]  

