FROM golang:1.9  
WORKDIR /go/src/github.com/drone-plugins/drone-ecr  
ADD . .  
RUN go get -u github.com/golang/dep/cmd/dep && \  
dep ensure && \  
GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build \  
-tags netgo -o /bin/drone-ecr \  
github.com/drone-plugins/drone-ecr  
  
FROM plugins/docker:latest  
COPY \--from=0 /bin/drone-ecr /bin/  
ENTRYPOINT ["/usr/local/bin/dockerd-entrypoint.sh", "/bin/drone-ecr"]  

