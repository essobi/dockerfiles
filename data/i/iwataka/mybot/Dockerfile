FROM golang:1.8-alpine  
  
WORKDIR /mybot  
  
RUN apk add --no-cache git  
# https://github.com/kubernetes/kubernetes/issues/39583  
RUN git config --global http.https://gopkg.in.followRedirects true  
RUN go get -u github.com/golang/dep/cmd/dep  
RUN go get github.com/iwataka/mybot  
RUN cd $GOPATH/src/github.com/iwataka/mybot && dep ensure && go build  
  
CMD cd $GOPATH/src/github.com/iwataka/mybot && mybot serve -H 0.0.0.0  
  
EXPOSE 8080  

