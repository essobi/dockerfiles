FROM golang:1.7-alpine  
MAINTAINER Yuta OHWATARI <yyutao88@gmail.com>  
  
ENV VERSION 0.0.8  
RUN apk update  
RUN apk add \  
gcc \  
ca-certificates \  
openssl \  
musl-dev \  
fuse \  
git \  
curl  
  
RUN mkdir -p ${GOPATH}/src/github.com/kahing  
RUN curl -L https://github.com/kahing/goofys/archive/v${VERSION}.tar.gz | tar
zxv -C ${GOPATH}/src/github.com/kahing  
RUN mv ${GOPATH}/src/github.com/kahing/goofys-${VERSION}
${GOPATH}/src/github.com/kahing/goofys  
WORKDIR ${GOPATH}/src/github.com/kahing/goofys  
RUN go get -d -v ./...  
RUN go install  
  
ENTRYPOINT ["goofys"]  
CMD ["--help"]  

