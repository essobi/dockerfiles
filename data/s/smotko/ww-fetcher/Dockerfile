FROM golang:1.4  
WORKDIR /go  
RUN mkdir gofetch  
RUN echo $GOPATH  
ENV PATH=$PATH:bin/:/go/gofetch/bin  
ENV GOPATH=$GOPATH:/go:/go/gofetch  
RUN go get github.com/tools/godep  
RUN go get github.com/jinzhu/gorm  
  
WORKDIR /go/gofetch/src/gofetch/  
ADD . /go/gofetch  
RUN go get  
  
WORKDIR /go/gofetch/src/  
CMD go run main.go  

