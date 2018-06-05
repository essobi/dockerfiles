FROM alpine:latest  
  
RUN apk add --no-cache python3 libacl  
RUN apk add --no-cache --virtual=build-dependencies wget ca-certificates
build-base acl-dev python3-dev openssl-dev && \  
wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python3 && \  
pip3 install attic && \  
apk del build-dependencies  
  
VOLUME /root/.attic  
VOLUME /root/.cache/attic  
  
ENTRYPOINT ["attic"]  

