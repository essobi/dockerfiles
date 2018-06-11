FROM centos:7  
  
MAINTAINER Sergio Jimenez <tripledes@gmail.com>  
  
ENV GOLANG_VERSION 1.6.1  
ENV GOPATH /go  
ENV GOROOT /opt/go  
ENV PATH $PATH:$GOROOT/bin  
  
COPY files/docker.repo /etc/yum.repos.d/docker.repo  
  
RUN yum update -y && \  
yum install -y wget git docker-engine-1.11.0-1.el7.centos.x86_64 rpm-plugin-
systemd-inhibit.x86_64 systemd-devel.x86_64 gcc && \  
yum clean all && \  
wget -q "https://storage.googleapis.com/golang/go$GOLANG_VERSION.linux-
amd64.tar.gz" -O /tmp/golang.tar.gz && \  
mkdir -p /go/src && \  
tar zxfp /tmp/golang.tar.gz -C /opt  
  
COPY scripts/run.sh /run.sh  
  
VOLUME ["/go/src"]  
  
CMD ["/run.sh"]  

