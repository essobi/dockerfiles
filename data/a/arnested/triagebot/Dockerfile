FROM golang:1.10-alpine AS build-env  
WORKDIR /go/src/github.com/arnested/triagebot  
COPY *.go /go/src/github.com/arnested/triagebot  
COPY jira /go/src/github.com/arnested/triagebot/jira  
COPY vendor /go/src/github.com/arnested/triagebot/vendor  
  
ENV CGO_ENABLED=0  
ENV GOOS=linux  
  
RUN go version  
RUN go build  
  
FROM scratch  
  
ENV PATH=/  
  
COPY \--from=build-env /usr/local/go/lib/time/zoneinfo.zip
/usr/local/go/lib/time/zoneinfo.zip  
COPY \--from=build-env /etc/ssl/certs/ /etc/ssl/certs/  
COPY \--from=build-env /go/src/github.com/arnested/triagebot/triagebot
/triagebot  
  
ENTRYPOINT ["triagebot"]  

