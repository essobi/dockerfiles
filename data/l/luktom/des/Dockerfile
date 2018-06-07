FROM alpine:latest  
  
VOLUME ["/data"]  
  
RUN apk update && apk add ca-certificates wget tar && rm -rf
/var/lib/apt/lists* && update-ca-certificates  
  
COPY download_and_extract /  
  
ENTRYPOINT ["/download_and_extract"]  

