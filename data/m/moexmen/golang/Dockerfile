FROM golang:1.9-alpine  
  
ENV GOOS linux  
ENV GOARCH amd64  
ENV CGO_ENABLED 0  
  
RUN apk --update add build-base git bash \  
&& go get -v -u github.com/stretchr/testify \  
github.com/tebeka/go2xunit \  
github.com/t-yuki/gocover-cobertura \  
gopkg.in/alecthomas/gometalinter.v2 \  
github.com/moexmen/gas-report-filter \  
&& gometalinter.v2 --install \  
# Needs to be installed last to override outdated version in gometalinter  
&& go get github.com/GoASTScanner/gas/cmd/gas/...  
  
COPY go-test-coverage-lint go-ast-scanner /usr/local/bin/  

