FROM golang  
MAINTAINER Wilmot Guillaume - Quorums  
  
RUN go get github.com/tools/godep  
  
ADD . /go/src/github.com/quorumsco/oauth2  
  
WORKDIR /go/src/github.com/quorumsco/oauth2  
  
RUN godep go build  
  
EXPOSE 8080  
ENTRYPOINT ["./oauth2"]  

