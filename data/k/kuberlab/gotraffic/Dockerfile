FROM golang:1.7.1  
RUN mkdir -p "$GOPATH/src/github.com/kuberlab/gotraffic"  
  
COPY . "$GOPATH/src/github.com/kuberlab/gotraffic"  
  
RUN go install "github.com/kuberlab/gotraffic"  
  
CMD [ "gotraffic" ]  
  
EXPOSE 8082  

