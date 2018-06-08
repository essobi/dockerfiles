FROM golang as builder  
WORKDIR /go/src/github.com/oscp/cloud-selfservice-portal-backend  
COPY . .  
RUN go get -v ./server  
  
FROM centos:7  
COPY \--from=builder /go/bin/server /usr/local/bin  
EXPOSE 8080  
ENTRYPOINT server  

