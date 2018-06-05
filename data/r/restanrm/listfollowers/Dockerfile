FROM golang:alpine  
  
ENV GOPATH /go  
  
RUN apk add \--update git  
RUN adduser -D golang && \  
chown golang: /go -R  
USER golang  
RUN go get github.com/restanrm/twitter  
RUN go get github.com/restanrm/listFollowers  
  
  
CMD listFollowers  

