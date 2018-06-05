FROM alpine:latest  
MAINTAINER Evan Verworn <spam@verworn.ca>  
  
RUN apk add \--no-cache python3 libacl  
RUN apk add \--no-cache \--virtual=build-dependencies wget ca-certificates
build-base acl-dev python3-dev openssl-dev && \  
wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python3 && \  
pip3 install attic && \  
apk del build-dependencies  
  
ENV ATTIC_UNKNOWN_UNENCRYPTED_REPO_ACCESS_IS_OK=yes  
  
ENTRYPOINT ["attic"]  

