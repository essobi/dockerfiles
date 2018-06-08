FROM golang:1.9-alpine  
  
CMD /bin/bash --login  
  
RUN echo "PATH=$PATH" > ~/.profile \  
&& apk add \--no-cache git openssh bash \  
&& go get -u golang.org/x/tools/cmd/goimports \  
&& go get -u github.com/golang/dep/cmd/dep  

