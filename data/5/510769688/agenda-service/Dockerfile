FROM golang:1.8  
COPY . "$GOPATH/src/github.com/LeungChiHo/Agenda-Service"  
RUN cd "$GOPATH/src/github.com/LeungChiHo/Agenda-Service/cli" && go get -v &&
go install -v  
RUN cd "$GOPATH/src/github.com/LeungChiHo/Agenda-Service/service" && go get -v
&& go install -v  
WORKDIR /  
EXPOSE 8080  
VOLUME ["/data"]

