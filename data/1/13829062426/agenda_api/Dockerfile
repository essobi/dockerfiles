FROM golang:latest  
WORKDIR /  
ADD . "$GOPATH/src/github.com/ZhangZeMian/agenda_api"  
RUN cd "$GOPATH/src/github.com/ZhangZeMian/agenda_api/cli/agenda" && go get -v
&& go install  
RUN cd "$GOPATH/src/github.com/ZhangZeMian/agenda_api/service" && go get -v &&
go install  
EXPOSE 8080  
VOLUME ["/data"]

