FROM golang:latest  
  
ADD . /go/src/github.com/SudoQ/scoop-hn-submitter  
ADD ./hn /go/src/github.com/SudoQ/scoop-hn-submitter/hn  
  
RUN go get "gopkg.in/redis.v3"  
  
RUN go install github.com/SudoQ/scoop-hn-submitter  
  
ENTRYPOINT /go/bin/scoop-hn-submitter  
  
EXPOSE 8080  

