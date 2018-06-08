FROM ubuntu:14.04  
MAINTAINER Aleksandr Tishin "atishin@cloudlinux.com"  
# Does not work with newer docker versions.  
# Starting from docker 1.6 there is an --ulimit option for docker run.  
# RUN ulimit -n 65536  
RUN apt-get update && \  
apt-get install -y curl && \  
apt-get install -y -q libcurl4-openssl-dev make && \  
apt-get clean  
  
RUN /usr/bin/curl -L http://toolbelt.treasuredata.com/sh/install-ubuntu-
trusty-td-agent2.sh | sh  
  
RUN sed -i -e "s/USER=td-agent/USER=root/" -e "s/GROUP=td-agent/GROUP=root/"
/etc/init.d/td-agent  
  
RUN /usr/sbin/td-agent-gem install fluent-plugin-elasticsearch --version 1.8.0  
RUN /usr/sbin/td-agent-gem install fluent-plugin-record-reformer --version
0.8.2  
  
WORKDIR /root  
  
EXPOSE 5140/udp  
  
ADD run.sh /root/  
ADD fluentd.conf.template /root/  
COPY filter_digestadd.rb /etc/td-agent/plugin/  
ADD syslog_index_template.json /root/  
ADD docker_index_template.json /root/  
  
CMD ./run.sh  

