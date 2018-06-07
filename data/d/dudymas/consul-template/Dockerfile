FROM debian:latest  
MAINTAINER Jeremy White <dudymas@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update -qq && \  
apt-get -y install curl runit && \  
rm -rf /var/lib/apt/lists/* && \  
curl -L https://github.com/hashicorp/consul-
template/releases/download/v0.8.0/consul-template_0.8.0_linux_amd64.tar.gz \  
| tar -C /usr/local/bin --strip-components 1 -zxf -  
  
COPY consul-template.service /etc/service/consul-template/run  
COPY run.sh run.sh  
  
ENV TEMPLATE_PATH=/etc/consul-templates/conf \  
SERVICE_PATH=/etc/service \  
TEMPLATE_TARGET_PATH=/etc/target/conf \  
CONSUL_HOST=consul.service.stack1 \  
"ON_RENDERER=echo restart" \  
CONSUL_PORT=8500  
  
CMD ./run.sh  
  

