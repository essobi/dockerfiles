FROM golang  
  
ADD . /go/src/github.com/jpkunkler/jpk_go  
WORKDIR /go/src/github.com/jpkunkler/jpk_go  
RUN go get  
RUN go install  
ENTRYPOINT /go/bin/jpk_go  
  
EXPOSE 8080

