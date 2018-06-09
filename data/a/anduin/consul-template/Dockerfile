FROM ubuntu:14.04  
MAINTAINER ductamnguyen@anduintransact.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install supervisor  
RUN apt-get update -y && apt-get install -y --no-install-recommends wget
supervisor ca-certificates unzip  
  
# Install consul-template  
RUN wget -O consul-template.zip https://releases.hashicorp.com/consul-
template/0.15.0/consul-template_0.15.0_linux_amd64.zip \  
&& unzip consul-template.zip \  
&& mv consul-template /usr/local/bin \  
&& rm -rf consul-template.zip  

