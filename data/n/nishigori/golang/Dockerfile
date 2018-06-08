# DOCKER-VERSION ~> 1.0.0  
# AUTHOR: Takuya Nishigori <nishigori.tak@gmail.com>  
# TO_BUILD: docker build -t my/app .  
FROM centos:latest  
  
RUN yum -y update && yum install -y curl tar gcc gcc-c++ kernel-devel git
mercurial bzr  
  
# Install Go (this is copied from the docker Dockerfile)  
RUN mkdir /goroot && curl https://storage.googleapis.com/golang/go1.3.linux-
amd64.tar.gz | tar xvzf - -C /goroot --strip-components=1  
RUN mkdir /gopath  
  
ENV GOROOT /goroot  
ENV GOPATH /gopath  
ENV CGO_ENABLED 0  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
# Smoke test  
RUN cd /tmp && echo 'package main' > t.go && go test -a -i -v  

