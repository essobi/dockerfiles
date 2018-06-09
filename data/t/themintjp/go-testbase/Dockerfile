FROM golang:1.10-alpine  
  
RUN apk --no-cache --update add \  
git \  
make \  
;  
RUN go get github.com/tenntenn/deppkg/cmd/deppkg  
RUN go get github.com/golang/dep/cmd/dep  

