FROM golang:1.8.3-alpine3.6 AS gobuild  
  
WORKDIR /  
ENV GOPATH="/"  
RUN apk update && apk add git  
COPY . .  
  
RUN go get -u github.com/me-box/GitHubReleaseTool  
RUN addgroup -S ghr && adduser -S -g ghr ghr  
RUN GGO_ENABLED=0 GOOS=linux go build -a -tags netgo -installsuffix netgo \  
-ldflags '-d -s -w -extldflags "-static"' \  
-o ghrelease ghrelease.go  
  
FROM scratch  
COPY \--from=gobuild /etc/passwd /etc/passwd  
COPY \--from=gobuild /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/ca-
certificates.crt  
  
USER ghr  
WORKDIR /  
COPY \--from=gobuild /ghrelease .  
  
ENTRYPOINT ["./ghrelease"]  

