FROM alpine:latest  
MAINTAINER lebokus "christian.lecherbauer@googlemail.com"  
RUN apk update  
RUN apk upgrade  
RUN apk add --no-cache bash git curl openssh openssl ca-certificates  
RUN update-ca-certificates  
  
RUN wget -qO- https://github.com/rancher/cli/releases/download/v0.6.7/rancher-
linux-amd64-v0.6.7.tar.gz | tar xvz  
RUN mv $(find . -name "rancher") /usr/local/bin  
RUN rm -Rf rancher-  
  
RUN wget https://github.com/lebokus/rancher-deploy/raw/master/rancher-deploy  
RUN mv rancher-deploy /usr/local/bin  
RUN chmod +x /usr/local/bin/rancher-deploy  

