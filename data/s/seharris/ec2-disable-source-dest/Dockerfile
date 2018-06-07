# Stage: build  
FROM golang:alpine AS build  
  
RUN apk add --no-cache git upx  
  
WORKDIR /go/src/app  
COPY *.go ./  
RUN go get -d -v ./...  
  
RUN CGO_ENABLED=0 go build -o disable-check -v main.go  
RUN upx --brute disable-check  
  
# Stage: package  
FROM scratch  
LABEL maintainer="Ruben Vermeersch <ruben@rocketeer.be>"  
# NB: We deliberately don't place this file in a directory normally  
# searched by Go's "crypto/x509" package, so that overriding the  
# SSL_CERT_FILE environment variable will not allow the package to  
# mistakenly still include this file anyway.  
COPY \--from=build /etc/ssl/certs/ca-certificates.crt /certs/  
ENV SSL_CERT_FILE /certs/ca-certificates.crt  
COPY \--from=build /go/src/app/disable-check /  
ENTRYPOINT ["/disable-check"]  

