FROM golang:alpine  
MAINTAINER Stephen Price <stephen@stp5.net>  
  
ENV RUNDECK_URL=http://rundeck:4440 \  
GOPATH=/go:/src/go-rundeck \  
BUILD_DEPS="git tar curl make"  
  
RUN apk --update add ${BUILD_DEPS} && \  
mkdir -p /src/go-rundeck && \  
curl -sL https://github.com/lusis/go-rundeck/archive/master.tar.gz | \  
tar -zxf - --strip-components=1 -C /src/go-rundeck && \  
cd /src/go-rundeck && \  
make all && \  
cp bin/* /usr/local/bin/ && \  
cd \- && \  
rm -rf /src/go-rundeck && \  
apk del ${BUILD_DEPS} && \  
rm -rf /var/cache/apk/*  

