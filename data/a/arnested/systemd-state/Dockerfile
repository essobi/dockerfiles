FROM golang:1.10-alpine AS build-env  
WORKDIR /go/src/github.com/arnested/systemd-state  
COPY *.go /go/src/github.com/arnested/systemd-state/  
COPY vendor /go/src/github.com/arnested/systemd-state/vendor  
  
ENV CGO_ENABLED=0  
ENV GOOS=linux  
  
RUN go version  
RUN go build  
RUN go test -o ./systemd-state.test -v -cover  
  
FROM scratch  
  
EXPOSE 80  
ENV PATH=/  
COPY \--from=build-env /go/src/github.com/arnested/systemd-state/systemd-state
/systemd-state  
COPY \--from=build-env /go/src/github.com/arnested/systemd-state/systemd-
state.test /test  
  
HEALTHCHECK CMD ["/systemd-state", "-healthcheck"]  
  
ENTRYPOINT ["systemd-state"]  

