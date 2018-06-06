FROM centos:latest  
  
MAINTAINER Kumulus Technologies <info@kumul.us>  
  
# Ensure there are enough file descriptors for running Fluentd.  
RUN ulimit -n 65536  
  
RUN rpm --import https://packages.treasuredata.com/GPG-KEY-td-agent  
  
ADD td-agent.repo /etc/yum.repos.d/td-agent.repo  
RUN yum -y update && yum -y install gem ruby-devel make gcc gcc-c++ net-tools
td-agent libcurl-devel && yum clean all  
RUN td-agent-gem install \  
docker-api \  
fluent-plugin-kubernetes \  
fluent-plugin-record-reformer \  
fluent-plugin-secure-forward \  
fluent-plugin-kubernetes_metadata_filter \  
fluent-plugin-systemd  
ADD ./in_cadvisor.rb /etc/td-agent/plugin/  
ADD ./run.sh /run.sh  
  
ENTRYPOINT ["/run.sh"]  

