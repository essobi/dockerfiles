FROM golang:1.6-alpine  
  
RUN apk add --update gcc git make libc-dev && rm -rf /var/cache/apk/*  
  
ENV GO15VENDOREXPERIMENT 1  
WORKDIR /root/work  
RUN go get -u -tags nopkcs11 github.com/cloudflare/cfssl/cmd/cfssl && go get
-u github.com/cloudflare/cfssl/cmd/cfssljson  
  
WORKDIR /root/work/tls  
ENTRYPOINT ["make"]  

