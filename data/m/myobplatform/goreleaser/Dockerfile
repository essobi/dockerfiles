FROM golang:1.9-alpine  
  
RUN apk add --no-cache git curl  
RUN curl -L
https://github.com/goreleaser/goreleaser/releases/download/v0.32.0/goreleaser_Linux_x86_64.tar.gz
| tar zx -C /usr/local/bin/  
ENTRYPOINT [ "goreleaser" ]

