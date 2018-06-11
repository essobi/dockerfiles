FROM golang:1.10.0-alpine3.7 AS compile  
WORKDIR /go/src/github.com/utopia-planitia/docker-image-builder/  
RUN apk --no-cache add git  
COPY . worker  
RUN CGO_ENABLED=0 GOOS=linux go install -a -installsuffix cgo ./worker  
  
FROM scratch  
COPY \--from=compile /go/bin/worker /worker  
ENTRYPOINT [ "/worker"]  

