FROM debian:7  
MAINTAINER Tacit Knowledge <operator@tacitknowledge.com>  
  
RUN apt-get -yqq update && apt-get -yqq install curl lsb-release vim less
locales procps net-tools && \  
curl -L https://www.opscode.com/chef/install.sh | bash -s -- -v 12.19.36 && \  
apt-get -yqq clean  
  
COPY files /  
ENV LANG=en_US.UTF-8  
RUN locale-gen  

