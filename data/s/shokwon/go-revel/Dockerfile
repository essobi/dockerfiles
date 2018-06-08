FROM golang:1.7.4  
RUN mkdir -p /go/src/hellogo  
ADD . /go/src/hellogo  
  
RUN go get github.com/revel/revel  
RUN go get github.com/revel/cmd/revel  
RUN revel build hellogo dev  
  
WORKDIR /go  
ENTRYPOINT dev/run.sh  
EXPOSE 9000  

