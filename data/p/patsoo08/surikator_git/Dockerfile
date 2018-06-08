FROM golang  
  
RUN go get -d -v github.com/sebastienmusso/infradatamgmt  
  
WORKDIR /go/src/github.com/sebastienmusso/infradatamgmt  
RUN git checkout patty  
RUN go get  
RUN go build -o surikator  
RUN cd rooter && go test  
  
CMD ["./surikator"]  

