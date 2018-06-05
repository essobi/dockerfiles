# golang-s2i  
FROM centos:7  
MAINTAINER Kenneth D. Evensen <kevensen@redhat.com>  
  
ARG GO_VERSION=1.6.2  
ENV BUILDER_VERSION 1.0  
ENV HOME /opt/app-root  
ENV GOPATH $HOME/gopath  
ENV GOBIN $GOPATH/bin  
ENV GOROOT $HOME/go  
ENV PATH $PATH:$GOROOT/bin:$GOBIN  
  
LABEL io.k8s.description="Platform for building go based programs" \  
io.k8s.display-name="gobuilder 0.0.1" \  
io.openshift.expose-services="8080:http" \  
io.openshift.tags="gobuilder,0.0.1" \  
io.openshift.s2i.scripts-url="image:///usr/local/s2i" \  
io.openshift.s2i.destination="/opt/app-root/destination"  
  
RUN yum clean all && \  
yum install -y tar \  
git-bzr && \  
yum clean all && \  
rm -rf /var/cache/yum/*  
  
COPY ./.s2i/bin/ /usr/local/s2i  
RUN useradd -u 1001 -r -g 0 -d ${HOME} -s /sbin/nologin -c "Default
Application User" default && \  
mkdir -p /opt/app-root/destination/{src,artifacts} && \  
curl -o $HOME/go${GO_VERSION}.linux-amd64.tar.gz
https://storage.googleapis.com/golang/go${GO_VERSION}.linux-amd64.tar.gz && \  
tar -C $HOME -xvf $HOME/go${GO_VERSION}.linux-amd64.tar.gz && \  
rm -f $HOME/go${GO_VERSION}.linux-amd64.tar.gz && \  
chown -R 1001:0 $HOME && chmod -R og+rwx ${HOME}  
  
WORKDIR ${HOME}  
USER 1001  
EXPOSE 8080  

