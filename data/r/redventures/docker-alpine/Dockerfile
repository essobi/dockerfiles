FROM gliderlabs/alpine:3.3  
  
# ca-certificates package is needed for HTTPS communication  
  
RUN apk update && apk add \--no-cache ca-certificates curl  
  
# This is needed for go binaries to run properly on alpine linux since the
binary needs libc and alpine use musl.  
  
RUN mkdir /lib64 && ln -s /lib/libc.musl-x86_64.so.1 /lib64/ld-
linux-x86-64.so.2  

