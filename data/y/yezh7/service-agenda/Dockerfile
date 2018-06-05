FROM golang:1.8  
COPY . "$GOPATH/src/github.com/James-Yip/service-agenda"  
RUN cd "$GOPATH/src/github.com/James-Yip/service-agenda/cli" && go get -v &&
go install -v  
RUN cd "$GOPATH/src/github.com/James-Yip/service-agenda/service" && go get -v
&& go install -v  
WORKDIR /  
EXPOSE 8080  
VOLUME ["/data"]  

