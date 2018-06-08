FROM golang:alpine as build-env  
RUN apk --no-cache add git  
  
RUN mkdir -p /go/src/github.com/syncthing/syncthing  
  
WORKDIR /go/src/github.com/syncthing/syncthing/  
  
ENV VERSION v0.14.44  
RUN git clone https://github.com/syncthing/syncthing.git . && git checkout
$VERSION  
  
RUN go run build.go build strelaysrv  
  
FROM alpine  
  
MAINTAINER Alessandro Lucaferro <alessandro.lucaferro@gmail.com>  
  
RUN apk --no-cache add ca-certificates curl && update-ca-certificates  
  
RUN mkdir strelaysrv  
  
WORKDIR /strelaysrv  
  
COPY \--from=build-env /go/src/github.com/syncthing/syncthing/strelaysrv
/strelaysrv/strelaysrv  
  
#HEALTHCHECK CMD curl -sS --silent --fail http://localhost:22070/status ||
exit 1  
EXPOSE 22067 22070  
ENTRYPOINT ["/strelaysrv/strelaysrv"]  

