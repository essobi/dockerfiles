FROM golang:alpine  
  
COPY . /go/src/gost  
  
RUN apk add --update git \  
&& cd /go/src/gost && go get -v -u ./... \  
&& CGO_ENABLED=0 go install -ldflags "-s -w" \  
&& mv /go/bin/gost /scramble  
  
FROM alpine:latest  
  
ENV SC_PROTO ss+ws  
ENV SC_MODE aes-128-cfb  
ENV SC_PASSWORD 123456789  
ENV SC_FAILSAFE "https://www.google.com"  
EXPOSE 8000  
COPY \--from=0 /scramble .  
CMD ./scramble -L=${SC_PROTO}://${SC_MODE}:${SC_PASSWORD}@:8000
-FS=${SC_FAILSAFE}

