FROM golang:1.10.2 AS build-env  
  
RUN mkdir -p /go/src/github.com/cloudflare && \  
cd /go/src/github.com/cloudflare && \  
git clone https://github.com/cloudflare/cloudflare-go && \  
cd cloudflare-go && \  
git checkout v0.8.5 && \  
go get github.com/cloudflare/cloudflare-go/cmd/flarectl  
RUN CGO_ENABLED=0 GOOS=linux go install -a -installsuffix cgo
github.com/cloudflare/cloudflare-go/cmd/flarectl  
  
FROM alpine:3.7  
RUN apk add \--no-cache ca-certificates curl  
COPY --from=build-env /go/bin/flarectl /bin/flarectl  
ENTRYPOINT ["/flarectl"]  
COPY cleanup add-node remove-node /bin/  

