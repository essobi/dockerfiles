FROM golang:1.6-alpine  
  
VOLUME /cfssl  
  
WORKDIR /cfssl  
  
ADD scripts/wrappers /wrappers  
ADD scripts/dump-wrappers /usr/local/bin  
  
RUN apk add --update git build-base && \  
go get -u -tags nopkcs11 github.com/cloudflare/cfssl/cmd/... && \  
apk del git build-base && \  
rm -rf /var/cache/apk/* && \  
chmod +x /usr/local/bin/dump-wrappers  
  
ENTRYPOINT [ "" ]  

