FROM golang:latest  
  
ADD . $GOPATH/src/github.com/itshappyhoursomewhere/backend  
RUN cd $GOPATH/src/github.com/itshappyhoursomewhere/backend/cmd/backend && go
get ./...  
RUN cd $GOPATH/src/github.com/itshappyhoursomewhere/backend/cmd/backend && go
install  
  
ENTRYPOINT ["backend"]

