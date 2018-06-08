FROM golang:1.10-alpine  
  
RUN apk add --no-cache --virtual .glide ca-certificates curl git && \  
curl -o glide.zip -L
https://github.com/Masterminds/glide/releases/download/v0.13.1/glide-v0.13.1-linux-
amd64.zip && \  
unzip glide.zip && \  
mv linux-amd64/glide $GOPATH/bin/glide && \  
rm -r linux-amd64 glide.zip  

