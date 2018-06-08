FROM golang:1.10 AS builder  
  
WORKDIR /go/src/github.com/majst01/periscope/  
  
COPY . /go/src/github.com/majst01/periscope/  
RUN apt update \  
&& apt install -y \  
libsystemd-dev \  
build-essential \  
libssl-dev \  
&& go get -u github.com/golang/dep/cmd/dep \  
&& make dep all \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt install -y nodejs \  
&& npm install \  
&& node_modules/.bin/webpack -p \  
&& rm -rf node_modules  
  
FROM debian:9-slim  
  
COPY \--from=builder /go/src/github.com/majst01/periscope/periscope
/periscope/  
COPY \--from=builder /go/src/github.com/majst01/periscope/static
/periscope/static  
  
WORKDIR /periscope  
  
CMD ["/periscope/periscope"]  

