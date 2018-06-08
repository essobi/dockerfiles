FROM alpine:3.2  
  
RUN apk add --update wget ca-certificates && \  
wget https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/2.23-r1/glibc-2.23-r1.apk \  
https://github.com/andyshinn/alpine-pkg-glibc/releases/download/2.23-r1/glibc-
bin-2.23-r1.apk && \  
apk add --allow-untrusted glibc-2.23-r1.apk glibc-bin-2.23-r1.apk && \  
apk del wget ca-certificates && \  
rm -rf glibc-2.23-r1.apk glibc-bin-2.23-r1.apk /var/cache/apk/*  

