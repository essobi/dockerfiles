FROM frolvlad/alpine-oraclejdk8:latest  
  
RUN apk add \--update python && \  
apk add bash wget ca-certificates && \  
wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python && \  
apk del wget ca-certificates && \  
rm /var/cache/apk/*  

