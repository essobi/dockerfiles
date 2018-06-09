FROM golang:1.10.0-alpine3.7 AS compile  
WORKDIR /go/src/github.com/utopia-planitia/  
COPY . nexus-gitlab-trigger  
RUN go test ./nexus-gitlab-trigger  
RUN CGO_ENABLED=0 GOOS=linux go install -a -installsuffix cgo ./nexus-gitlab-
trigger  
  
FROM scratch  
COPY \--from=compile /go/bin/nexus-gitlab-trigger /nexus-gitlab-trigger  
ENTRYPOINT [ "/nexus-gitlab-trigger"]  

