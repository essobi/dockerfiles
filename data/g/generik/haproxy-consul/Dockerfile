FROM alpine  
  
MAINTAINER Steven Borrelli <steve@aster.is>  
MAINTAINER Mateusz Pawlowski <mateusz@generik.co.uk>  
LABEL kind=proxy config_source=consul  
  
ENV CONSUL_TEMPLATE_VERSION=0.12.2  
RUN apk --update add bash haproxy ca-certificates unzip  
  
ADD https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /  
  
RUN unzip /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip && \  
mv /consul-template /usr/local/bin/consul-template && \  
rm -rf /consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip  
  
RUN mkdir -p /haproxy /consul-template/config.d /consul-template/template.d  
  
ADD config/ /consul-template/config.d/  
ADD template/ /consul-template/template.d/  
ADD launch.sh /launch.sh  
  
CMD ["/launch.sh"]  

