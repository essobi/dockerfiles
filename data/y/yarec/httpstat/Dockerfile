FROM golang:alpine  
  
# Install packages  
RUN \  
apk --update add git \  
&& rm -rf /var/cache/apk/* \  
&& go get -u github.com/davecheney/httpstat \  
&& apk del git  

