FROM node:0.12  
MAINTAINER Eric Chapman <eric@thehq.io>  
  
ENV CONSUL_TEMPLATE_VERSION 0.10.0  
ENV SERVICE_ENTRY app.js  
ENV ROUTER_PROTOCOL ws  
ENV ROUTER_SERVICE app.router  
ENV ROUTER_REALM realm1  
ENV CONSUL_SERVER consul.service.consul:8500  
# apt-get  
RUN apt-get update -y  
RUN apt-get install -y \  
runit  
  
RUN npm install \  
autobahn \  
\--save  
  
# Consul Templates  
RUN curl -L https://github.com/hashicorp/consul-
template/releases/download/v${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.tar.gz | tar -C /usr/local/bin
--strip-components 1 -zxf - \  
&& chmod +x /usr/local/bin/consul-template  
  
RUN mkdir /etc/consul-templates/  
COPY templates/*.tmpl /etc/consul-templates/  
  
# Copy any source code  
COPY src/ /app/src/  
  
# Create the services  
COPY services/ /etc/service/  
RUN chmod +x /etc/service/*/run  
  
# Run the services  
ENTRYPOINT ["runsvdir"]  
CMD ["/etc/service/"]

