FROM golang:1.9.2-alpine  
  
ENV DEP_VERSION 0.3.2  
RUN apk add --no-cache --virtual .build-deps \  
ca-certificates \  
git \  
wget && \  
update-ca-certificates  
  
RUN cd /usr/local/bin/ && \  
wget https://github.com/golang/dep/releases/download/v${DEP_VERSION}/dep-
linux-amd64 && \  
mv dep-linux-amd64 dep && \  
chmod 775 dep  

