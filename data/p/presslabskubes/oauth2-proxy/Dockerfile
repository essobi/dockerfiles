FROM golang:1.8-alpine as build-oauth2  
  
COPY patch.diff /root/  
  
RUN set -ex \  
&& apk add --no-cache git \  
&& mkdir -p ./src/github.com/bitly \  
&& cd ./src/github.com/bitly/ \  
&& git clone https://github.com/bitly/oauth2_proxy.git \  
&& cd oauth2_proxy \  
&& patch < /root/patch.diff \  
&& go get ./... \  
&& go build  
  
FROM alpine  
  
RUN set -ex \  
&& apk add --no-cache ca-certificates  
  
COPY \--from=build-oauth2 /go/src/github.com/bitly/oauth2_proxy/oauth2_proxy
/usr/local/bin/  
ENTRYPOINT ["oauth2_proxy"]  

