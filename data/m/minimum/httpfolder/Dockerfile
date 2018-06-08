FROM golang:1.6-alpine  
  
MAINTAINER minimum@cepave.com  
  
RUN \  
apk add --no-cache bash git \  
&& go get github.com/Cepave/httpfolder \  
&& cd $GOPATH/src/github.com/Cepave/httpfolder \  
&& go build  
  
EXPOSE 8080  
WORKDIR /www-data  
  
CMD $GOPATH/bin/httpfolder -p 8080 $USERNAME $PASSWORD  

