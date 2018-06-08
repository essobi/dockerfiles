FROM golang:1.8-alpine  
RUN apk --no-cache add ca-certificates  
WORKDIR /go/src/github.com/quintoandar/docker-drone-metronome-runner  
ADD . .  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o
/usr/local/bin/app .  
ENTRYPOINT ["app"]  
  

