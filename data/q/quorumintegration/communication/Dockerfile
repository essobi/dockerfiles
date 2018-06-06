FROM golang  
MAINTAINER Daniel Jean-Baptiste - Quorum Impact  
  
RUN go get github.com/tools/godep  
  
ADD . /go/src/bitbucket.org/quorumteam/communication  
  
WORKDIR /go/src/bitbucket.org/quorumteam/communication  
  
RUN godep go build  
  
EXPOSE 8080  
ENTRYPOINT ["./communication"]  

