FROM golang:1.6.2  
MAINTAINER Sproutling Inc. "devops@sproutling.com"  
RUN apt-get update -qq && apt-get install -y build-essential  
  
RUN go get -u github.com/tools/godep  
  
WORKDIR /go/src/github.com/Sproutling/dumb-app  
ADD . /go/src/github.com/Sproutling/dumb-app  
  
RUN godep restore  
RUN go install github.com/Sproutling/dumb-app  
  
ENV GOPATH /go  
  
CMD ["dumb-app"]  

