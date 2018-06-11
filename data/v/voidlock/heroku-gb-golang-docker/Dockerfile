FROM golang:1.4.2  
MAINTAINER Alex Arnell <alex.arnell@gmail.com>  
  
RUN go get github.com/constabulary/gb/...  
  
RUN mkdir -p /go/src/app  
WORKDIR /go/src/app  
  
CMD ["go-wrapper", "run"]  
  
ONBUILD COPY . /go/src/app  
ONBUILD RUN gb build  

