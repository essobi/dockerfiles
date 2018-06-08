FROM ubuntu:14.04  
MAINTAINER Takayuki Shimizukawa shimizukawa@gmail.com  
  
# environment  
ENV DEBIAN_FRONTEND noninteractive  
  
# update  
RUN apt-get update && apt-get -y upgrade  
  
# ruby related packages for td-agent  
RUN apt-get -y install curl libcurl4-openssl-dev ruby ruby-dev make  
  
# install fluentd td-agent  
RUN curl -L http://toolbelt.treasuredata.com/sh/install-ubuntu-trusty-td-
agent2.sh | sh  
  
# clean cache files  
RUN apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
# install fluentd plugins  
RUN /opt/td-agent/embedded/bin/fluent-gem install --no-ri --no-rdoc \  
fluent-plugin-elasticsearch \  
fluent-plugin-record-modifier \  
fluent-plugin-exclude-filter  
  
# add conf  
ADD ./etc/fluentd /etc/fluentd  
  
CMD /etc/init.d/td-agent stop && /opt/td-agent/embedded/bin/fluentd -c
/etc/fluentd/fluent.conf  

