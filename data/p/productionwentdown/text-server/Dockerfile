FROM golang:1.10-alpine as go  
  
WORKDIR /go/src/text-server  
COPY . .  
ENV CGO_ENABLED=0  
ENV GOOS=linux  
ENV GOARCH=amd64  
RUN go build -ldflags '-extldflags "-static"' -o text-server  
  
FROM scratch  
  
EXPOSE 8080  
COPY \--from=go /go/src/text-server/text-server text-server  
  
ENTRYPOINT ["/text-server"]  

