FROM alpine:3.3  
RUN apk update && \  
apk -Uuv add python py-pip && \  
pip install dynamic-dynamodb && \  
apk del py-pip && \  
rm -rf /var/cache/*  
  
ENTRYPOINT ["dynamic-dynamodb"]  

