FROM golang:1.4.2  
MAINTAINER YI-HUNG JEN <yihungjen@gmail.com  
  
COPY . /go/src/github.com/jeffjen/agent  
WORKDIR /go/src/github.com/jeffjen/agent  
  
ENV GOPATH /go/src/github.com/jeffjen/agent/Godeps/_workspace:$GOPATH  
RUN go install  
  
ENTRYPOINT ["agent"]  
CMD ["--help"]  

