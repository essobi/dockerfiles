FROM golang:1.8  
COPY . "$GOPATH/src/github.com/Sevennn/github.com/Sevennn/agenda-go-server"  
RUN cd "$GOPATH/src/github.com/Sevennn/github.com/Sevennn/agenda-go-
server/cli" && go get -v && go install -v  
RUN cd "$GOPATH/src/github.com/Sevennn/github.com/Sevennn/agenda-go-
server/service" && go get -v && go install -v  
WORKDIR /  
EXPOSE 8080  
VOLUME ["/data"]  

