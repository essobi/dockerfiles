# Dockerfile for adding etcd to a base image  
FROM ubuntu:latest  
  
MAINTAINER Vincent Palmer <shift-gh@someone.section.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y software-properties-common python-
software-properties  
RUN apt-get install -y curl  
  
RUN mkdir /tmp/etcd  
RUN curl --silent https://api.github.com/repos/coreos/etcd/releases | grep -v
beta | grep -v alpha | sed -n 's|.*\"tag_name\": \"\\(.*\\)\".*|\1|p' | head
-n 1 > /tmp/etcd_version  
RUN curl -L https://github.com/coreos/etcd/releases/download/`cat
/tmp/etcd_version`/etcd-`cat /tmp/etcd_version`-linux-amd64.tar.gz | tar -xz
--directory /tmp/etcd --strip-components 1  
RUN cp /tmp/etcd/etcd /usr/local/bin/ && cp /tmp/etcd/etcdctl /usr/local/bin/  
RUN rm -rf /tmp/etcd  

