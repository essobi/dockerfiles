FROM golang:1.9  
ADD . /go/src/github.com/fever-ch/go-google-sites-proxy  
WORKDIR /go/src/github.com/fever-ch/go-google-sites-proxy  
RUN go get ./...; go build -ldflags="-s -w -X main.GitVersion=$(git describe
--always --long --dirty) -X main.BuildDate=$(date +%Y-%m-%d/%H:%M:%S)"  
  
FROM alpine  
RUN apk add --no-cache ca-certificates  
COPY \--from=0 /go/src/github.com/fever-ch/go-google-sites-proxy/go-google-
sites-proxy /bin/go-google-sites-proxy  
ENTRYPOINT /bin/go-google-sites-proxy /etc/ggsp/config.yaml  
EXPOSE 9080  

