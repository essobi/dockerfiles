FROM golang:1.8  
COPY . "$GOPATH/src/github.com/Caroline1997/Service-Agenda"  
RUN cd "$GOPATH/src/github.com/Caroline1997/Service-Agenda/cli" && go get -v
&& go install -v  
RUN cd "$GOPATH/src/github.com/Caroline1997/Service-Agenda/service" && go get
-v && go install -v  
WORKDIR /  
EXPOSE 8080  
VOLUME [ "/data" ]

