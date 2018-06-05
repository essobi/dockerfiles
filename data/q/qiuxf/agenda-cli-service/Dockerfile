FROM golang:1.8  
COPY . "$GOPATH/src/agenda-cli-service"  
RUN cd "$GOPATH/src/agenda-cli-service/cli" && go get -v && go install -v  
RUN cd "$GOPATH/src/agenda-cli-service/service" && go get -v && go install -v  
WORKDIR /  
EXPOSE 8080  
VOLUME ["/data"]  

