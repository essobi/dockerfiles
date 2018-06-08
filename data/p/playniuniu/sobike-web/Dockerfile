FROM golang:latest as builder  
LABEL maintainer="playniuniu@gmail.com"  
  
COPY src/ /opt/src/  
  
RUN go get github.com/fatih/color \  
&& go get github.com/sirupsen/logrus \  
&& go get github.com/julienschmidt/httprouter \  
&& cd /opt/ \  
&& GOPATH=$GOPATH:`pwd` CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o
sobike-web -ldflags '-w -s' src/sobike-web.go  
  
FROM alpine:latest  
  
RUN apk add --update --no-cache curl \  
&& mkdir -p /opt/src/  
  
COPY \--from=builder /opt/sobike-web /opt/  
COPY \--from=builder /opt/src/webpage /opt/src/webpage  
  
EXPOSE 8080  
WORKDIR /opt/  
CMD [ "./sobike-web", "-p", "8080" ]  

