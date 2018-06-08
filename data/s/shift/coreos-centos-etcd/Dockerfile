# Dockerfile for adding etcd to a base image  
FROM centos:latest  
  
MAINTAINER Vincent Palmer <shift-gh@someone.section.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN yum install -y curl tar  
  
RUN mkdir /tmp/etcd  
RUN curl --silent https://api.github.com/repos/coreos/etcd/releases | sed -n
's|.*\"tag_name\": \"\\(.*\\)\".*|\1|p' | head -n 1 > /tmp/etcd_version  
RUN curl -L https://github.com/coreos/etcd/releases/download/`cat
/tmp/etcd_version`/etcd-`cat /tmp/etcd_version`-linux-amd64.tar.gz | tar -xz
--directory /tmp/etcd --strip-components 1  
RUN cp /tmp/etcd/etcd /usr/local/bin/ && cp /tmp/etcd/etcdctl /usr/local/bin/  
RUN rm -rf /tmp/etcd  

