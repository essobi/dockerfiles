FROM google/cloud-sdk:alpine  
  
MAINTAINER Kirill Garbar <kirill@iterium.co.uk>  
  
RUN apk --update upgrade \  
&& apk add go \  
&& rm /var/cache/apk/*  
  
ENV GOROOT /usr/lib/go  
ENV GOPATH /gopath  
ENV GOBIN /gopath/bin  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  

