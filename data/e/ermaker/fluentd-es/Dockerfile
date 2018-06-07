FROM ubuntu:14.04  
MAINTAINER Minwoo Lee "ermaker@gmail.com"  
# Ensure there are enough file descriptors for running Fluentd.  
RUN ulimit -n 65536  
  
# Install prerequisites.  
RUN apt-get update && \  
apt-get install -y curl && \  
apt-get install -y -q libcurl4-openssl-dev make && \  
apt-get clean  
  
# Install Fluentd.  
RUN /usr/bin/curl -L http://toolbelt.treasuredata.com/sh/install-ubuntu-
trusty-td-agent2.sh | sh  
  
# Change the default user and group to root.  
# Needed to allow access to /var/log/docker/... files.  
RUN sed -i -e "s/USER=td-agent/USER=root/" -e "s/GROUP=td-agent/GROUP=root/"
/etc/init.d/td-agent  
  
# Install Fluentd plug-in  
## Elasticsearch  
RUN /usr/sbin/td-agent-gem install fluent-plugin-elasticsearch  
## add hostname  
RUN /usr/sbin/td-agent-gem install fluent-plugin-hostname  
  
ENTRYPOINT ["/usr/sbin/td-agent"]  

