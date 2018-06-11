FROM wellsie/centos7  
MAINTAINER Jono Wells <_@oj.io>  
  
ENV VERSION 1.4.2  
ENV OS linux  
ENV ARCH amd64  
  
RUN yum -y install git tar \  
&& yum -y clean all  
  
ADD https://storage.googleapis.com/golang/go${VERSION}.${OS}-${ARCH}.tar.gz
/tmp/go${VERSION}.${OS}-${ARCH}.tar.gz  
  
RUN tar -C /usr/local -xzf /tmp/go${VERSION}.${OS}-${ARCH}.tar.gz \  
&& rm /tmp/go${VERSION}.${OS}-${ARCH}.tar.gz \  
&& mkdir -p /go/src/app  
  
ENV PATH $PATH:/usr/local/go/bin  
ENV GOPATH /go  

