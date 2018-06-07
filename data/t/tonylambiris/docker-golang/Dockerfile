FROM alpine:latest  
  
MAINTAINER Dustin Willis Webber  
  
ENV OS=linux ARCH=amd64 GO_VERSION=1.9.1 GOROOT=/usr/local/go GOPATH=/go  
ENV PATH="$GOPATH/bin:$GOROOT/bin:$PATH"  
  
RUN apk add \--no-cache autoconf automake bash curl gcc g++ git make rpm \  
python2 ruby ruby-dev nodejs nodejs-npm libc-dev libc6-compat libffi-dev \  
libpng-dev  
  
RUN curl -sSL https://golang.org/dl/go$GO_VERSION.$OS-$ARCH.tar.gz \  
| tar -C /usr/local -xz && strip /usr/local/go/bin/* && \  
mkdir -p /go /source && chmod -R 777 /go /source && \  
gem install fpm package_cloud thor-scmversion --no-ri \--no-rdoc && \  
go get -u github.com/kardianos/govendor  
  
WORKDIR /source  

