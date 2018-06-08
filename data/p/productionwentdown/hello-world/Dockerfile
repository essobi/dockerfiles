FROM golang:1.10-alpine as go  
  
WORKDIR /go/src/hello-world  
COPY . .  
ENV CGO_ENABLED=0  
ENV GOOS=linux  
ENV GOARCH=amd64  
RUN go build -ldflags '-extldflags "-static"' -o hello-world  
  
FROM scratch  
  
EXPOSE 8080  
COPY \--from=go /go/src/hello-world/hello-world hello-world  
  
ENTRYPOINT ["/hello-world"]  

