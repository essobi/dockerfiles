FROM golang:1.8  
RUN mkdir /data  
COPY . "$GOPATH/src/github.com/caijh23/GoAgenda/"  
RUN cd "$GOPATH/src/github.com/caijh23/GoAgenda/http-api" && go get -v && go
install -v  
RUN cd "$GOPATH/src/github.com/caijh23/GoAgenda/cli" && go get -v && go
install -v  
  
EXPOSE 8080  
VOLUME /data

