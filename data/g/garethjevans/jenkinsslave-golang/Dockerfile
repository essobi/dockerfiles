FROM garethjevans/jenkinsslave-alpine:v2.0-pre2  
  
USER root  
  
RUN apk update && \  
apk add bzr tree git go build-base && \  
rm -rf /var/cache/apk/*  
  
USER jenkins  

