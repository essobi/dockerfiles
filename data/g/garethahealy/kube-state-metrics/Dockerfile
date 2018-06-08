FROM centos:7  
MAINTAINER garethahealy (https://github.com/garethahealy/)  
  
LABEL Name="kube-state-metrics (https://github.com/kubernetes/kube-state-
metrics)" \  
Vendor="com.garethahealy" \  
Version="v0.3.0" \  
License="Apache License, Version 2.0"  
  
USER root  
  
# Compiler tools  
RUN yum install -y gcc kernel-devel make && \  
yum install -y git wget && \  
yum clean all  
  
# Install go-long  
RUN wget https://storage.googleapis.com/golang/go1.7.4.linux-amd64.tar.gz && \  
tar -xvf go1.7.4.linux-amd64.tar.gz && \  
mv go /usr/local  
  
# Setup go-lang enviroment  
ENV GOROOT=/usr/local/go  
ENV GOPATH=$HOME/go-projects  
ENV
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$GOPATH/bin:$GOROOT/bin  
  
# Build kube-state-metrics  
RUN mkdir -p $GOPATH/src && \  
cd $GOPATH/src && \  
git clone \--depth 1 --branch v0.3.0 https://github.com/kubernetes/kube-state-
metrics.git && \  
cd kube-state-metrics && \  
make build  
  
EXPOSE 9779  
ENTRYPOINT ["/go-projects/src/kube-state-metrics/kube-state-metrics", "--
port=9779"]  

