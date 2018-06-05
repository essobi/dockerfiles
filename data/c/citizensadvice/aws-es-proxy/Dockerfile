FROM golang:1.8.3-alpine3.6  
  
ENV REF='v0.4' \  
GO15VENDOREXPERIMENT=1  
  
RUN apk update && \  
apk add \--no-cache git glide openssl && \  
mkdir -p $GOPATH/src/github.com/abutaha && \  
cd $GOPATH/src/github.com/abutaha && \  
git clone https://github.com/abutaha/aws-es-proxy --depth 1 \--branch $REF &&
\  
cd aws-es-proxy && \  
glide install && \  
cd /bin && \  
apk del git glide && \  
rm -rf /var/cache/apk/* && \  
go build github.com/abutaha/aws-es-proxy  

