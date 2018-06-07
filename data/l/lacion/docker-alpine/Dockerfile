FROM golang:1.10.2-alpine  
MAINTAINER Luis Morales <luismmorales@gmail.com>  
  
ENV LANG=en_US.UTF-8  
  
RUN apk add --no-cache --update curl \  
bash \  
grep \  
sed \  
jq \  
ca-certificates \  
openssl \  
git \  
make \  
gcc \  
musl-dev  
  
RUN go get -u github.com/golang/dep/cmd/dep

