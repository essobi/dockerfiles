FROM alpine:3.6  
  
RUN apk add \--no-cache python && \  
apk add \--no-cache \--virtual=build-dependencies wget ca-certificates && \  
wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python && \  
apk del build-dependencies  
  
RUN pip install awscli  
  
ENTRYPOINT ["aws"]  
  

