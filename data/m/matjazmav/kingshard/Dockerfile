FROM golang:1.7-alpine  
  
ENV KINGSHARD_VERSION=1.5 \  
GO_VERSION=1.6 \  
PATH=$PATH:/usr/local/go/bin:/usr/local/kingshard/bin \  
GOPATH=/  
  
RUN apk add --no-cache bash git make && \  
git clone --branch $KINGSHARD_VERSION --depth 1
https://github.com/flike/kingshard.git /src/github.com/flike/kingshard && \  
/bin/bash -c "source /src/github.com/flike/kingshard/dev.sh" && \  
make -C /src/github.com/flike/kingshard && \  
mv /src/github.com/flike/kingshard/bin/kingshard /kingshard && \  
rm -rf /src && \  
apk del bash git make  
  
COPY ks.yaml /etc/ks.yaml  
  
ENTRYPOINT ["/kingshard"]  

