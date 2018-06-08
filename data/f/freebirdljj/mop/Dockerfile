FROM golang:latest  
MAINTAINER FreeBirdLjj  
  
RUN go get github.com/mop-tracker/mop && go install -x github.com/mop-
tracker/mop/cmd/mop && rm -fr $GOPATH/src/github.com  
  
ENTRYPOINT ["mop"]  

