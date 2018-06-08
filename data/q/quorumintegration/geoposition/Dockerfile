FROM golang  
MAINTAINER Daniel Jean-Baptiste - Quorum  
  
RUN go get github.com/tools/godep  
  
ADD . /go/src/bitbucket.org/quorumteam/geoposition  
  
WORKDIR /go/src/bitbucket.org/quorumteam/geoposition  
  
RUN godep go build  
  
EXPOSE 8080  
ENTRYPOINT ["./geoposition"]  

