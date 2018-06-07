# RUBY MACHINE  
FROM golang:1.4.0  
MAINTAINER Tiago Scolari <tscolari@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \--force-yes \  
tmux \  
ssh \  
vim \  
git-core \  
make && \  
apt-get clean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /go/src/github.com/tscolari &&\  
ln -s /workdir /go/src/github.com/tscolari/docode  
  
RUN go get github.com/onsi/ginkgo/ginkgo &&\  
go get github.com/onsi/gomega &&\  
go install github.com/onsi/ginkgo/ginkgo &&\  
go get gopkg.in/yaml.v2  
  

