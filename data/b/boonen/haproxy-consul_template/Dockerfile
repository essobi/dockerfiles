FROM haproxy:1.6.5-alpine  
MAINTAINER Jan Boonen <jan.boonen@geodan.nl>  
  
ENV CONSUL_TEMPLATE_HOME /opt/consul  
ENV CONSUL_TEMPLATE_VERSION 0.15.0  
ENV CONSUL_TEMPLATE_SHA256
b7561158d2074c3c68ff62ae6fc1eafe8db250894043382fb31f0c78150c513a  
ENV CONSUL_ADDRESS 127.0.0.1:8500  
RUN apk add --update curl unzip supervisor && \  
curl -SL "https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip" -o consul_template.zip \  
&& echo "${CONSUL_TEMPLATE_SHA256} consul_template.zip" | sha256sum -c \  
&& mkdir -p ${CONSUL_TEMPLATE_HOME} \  
&& unzip consul_template.zip -d ${CONSUL_TEMPLATE_HOME} \  
&& rm consul_template.zip \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /opt/supervisor  
  
ADD assets/supervisor.conf /opt/supervisor/  
ADD assets/haproxy.cfg /usr/local/etc/haproxy/  
  
CMD ["supervisord", "--nodaemon", "--configuration",
"/opt/supervisor/supervisor.conf"]  

