FROM sequenceiq/alpine-dev:3.1  
  
RUN apk -U add git mercurial go  
  
ENV GOPATH=/go  
RUN mkdir $GOPATH  
ENV PATH=$PATH:$GOPATH/bin  
  

